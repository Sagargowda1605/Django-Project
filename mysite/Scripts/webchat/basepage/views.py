from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from .models import Room,Topic,Messages
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#data=[
 #   {"id":1,"name":"Sagar_gowda","Age":23,"qualification":"none"},
  #  {"id":2,"name":"Dennis","Age":34,"qualification":"youtuber"},
 #   {"id":3,"name":"threveni","Age":30,"qualification":"PHD"}]


def loginview(request):

    page='login'

    if request.user.is_authenticated:
        return redirect('Home')
    
    if request.method=="POST":
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "User Not Found")
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request, "UserName Or Password Does not Match")

    context={
        'page':page
    }

    return render(request,'basepage/login_register.html',context)


def logoutview(request):
    logout(request)
    return redirect('Home')

def register(request):
    form=UserCreationForm()
    context={
        'form':form
    }
    if request.method=='POST':
        form=form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('Home') 
        else :
            messages.error(request, "Error occured")
    return render(request,'basepage/login_register.html',context)


def Home(request):
    q=request.GET.get('q')
    if request.GET.get('q')!=None:
        obj=Room.objects.filter(Q(topic__name__contains=q)|Q(name__contains=q)|Q(description__contains=q))
        #__ means refering to the parent so that means that name of parent topic refeing from the models check models
        #  you will get the idea conatins is used for the when you type the py it should show the topic from matchinh keywords 
        #topics=Topic.objects.all()
        #Room_count=obj.count()
        All_messages=Messages.objects.filter(Q(room__topic__name__icontains=q)).order_by('-updated')
    else:
        obj=Room.objects.all()
        #Room_count=obj.count()
        All_messages=Messages.objects.all().order_by('-updated')

    Room_count=obj.count()
    topics=Topic.objects.all() 
    context={'objects':obj,'topics':topics,'Room_count':Room_count,'Actvities_messages':All_messages}
    return  render(request,"basepage/Home.html",context)


def user_profile(request,pk):
    user=User.objects.get(id=pk)
    rooms=user.room_set.all()
    All_messages=user.messages_set.all()
    topics=Topic.objects.all() 
    context={
        'user':user,
        'objects':rooms,
        'Actvities_messages':All_messages,
        'topics':topics

    }

    return render(request,'basepage/profile.html',context)

def webroom(request):
    return render(request,"basepage/webroom.html")

def details(request,pk):
    obj=Room.objects.get(id=pk)
    conversations=obj.messages_set.all().order_by('-updated')
    participants=obj.participants.all()
    #.here messages is the model Messages to acess all the messages of relating room
    #  .messages_set is sued its pre defined method in django
    if request.method=='POST':
        message=Messages.objects.create(
            user=request.user,
            room=obj,
            body=request.POST.get('message_body')
        )
        obj.participants.add(request.user)
        return redirect('chatroom',pk=obj.id)
    context={
        'objects':obj,
        'conversation':conversations,
        "users":participants
    }

    return render(request,"basepage/details.html",context)


# decraters is used to restrict the user from certaing paages 
# here before login we dont want user cannot able to create the room so it will be directed to the login page 
@login_required(login_url='/login')
def create_Room(request):
    form=RoomForm
    if request.method=="POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.host=request.user
            room.save()
            return redirect('Home')
    context={
        'forms':form
    }
    return render(request,"basepage/Home_form.html",context)

@login_required(login_url='/login')
def update_Room(request,pk):
    obj=Room.objects.get(id=pk)
    form=RoomForm(instance=obj)

    if request.method=="POST":
        form=RoomForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Home')
    context={
        'forms':form
    }
    return render(request,'basepage/Home_form.html',context)

@login_required(login_url='/login')
def delete_Room(request,pk):
    obj=Room.objects.get(id=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('Home')
    context={
        'form':obj
    }
    return render(request,'basepage/delete.html',context)


@login_required(login_url='/login')
def delete_Message(request,pk):
    obj=Messages.objects.get(id=pk)
    obj.delete()
    previous_page = request.META.get('HTTP_REFERER', '/')
    
    # Redirect back to the same page
    return redirect(previous_page)


