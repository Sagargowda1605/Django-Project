from rest_framework.decorators import api_view
from rest_framework.response import Response
from basepage.models import Room
from .serializers import Roomserializer



@api_view(['GET'])
#if we want we use put, ptach delete all these requests
#like  these @api_view('GET',"PUT','Delete')
def get_routes(request):
    routes=[
        'GET/api',
        'GET/api/rooms',
        'GET/api/rooms/:id'
    ]

    return Response(routes)


@api_view(['GET'])
def get_rooms(request):
    obj=Room.objects.all()
    serializer=Roomserializer(obj,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_room(request,pk):
    obj=Room.objects.get(id=pk)
    serilizbale=Roomserializer(obj,many=False)
    return Response(serilizbale.data)