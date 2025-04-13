from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    #now here i dont want to delete the room when the topic gets deleted so i put for set_null value 
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    #here participans is many to many relation one user can join many rooms aldo one room can have many users
    # to use the many to many relations we have use the method ManyToManyField and
    #  because user also alreeady refered at host to name it different we have use the related name thing 
    updated=models.DateTimeField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    #auto_now_add just takes time when its created abd after that its doesnt chnage
    # but in the case of auto_now when time he saves times get upadted

    #class meta is added because we want to order the the things in spefic way, here - is added to get the descending order
    #if we dont add the - we will get in the ascending order 
    class Meta:
        ordering=['-updated','-created']

    # this method is used for the string reprensataion of object that we created model
    def __str__(self):
        return self.name
    
class Messages(models.Model):
    #user is on one-to-many relations 
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # This is refrence to the above Room model its interlinked thats why this is aforiegn key ots called one too-many relation 
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


