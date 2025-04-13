from django.urls import path

from .views import (Home,webroom,details,create_Room,update_Room,delete_Room,
loginview,logoutview,register,delete_Message,user_profile)

urlpatterns = [
    path('login/',loginview,name='user_login'),
    path('logout/',logoutview,name='logout'),
    path('register',register,name='user_register'),
    path('', Home,name="Home"),
    path('room/',webroom,name="webroom"),
    path('details/<int:pk>',details,name='chatroom'),
    path('createroom/',create_Room,name='createroom'),
    path('updateroom/<int:pk>',update_Room,name='updateroom'),
    path('deleteroom/<int:pk>',delete_Room,name='deleteroom'),
    path('deletemessage/<int:pk>',delete_Message,name='delete_message'),
    path('profile/<str:pk>',user_profile,name='profile')
]
