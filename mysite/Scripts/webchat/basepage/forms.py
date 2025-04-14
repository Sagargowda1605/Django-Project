from django.forms import ModelForm
from .models import Room ,User
from django.contrib.auth.forms import UserChangeForm

class RoomForm(ModelForm):


    class Meta:
        model=Room
        fields='__all__'
        exclude=['host','participants']


class UpdateUserForm(UserChangeForm):

    passowrd=None

    class meta:
        model=User
        fields=['email','username','description']

        