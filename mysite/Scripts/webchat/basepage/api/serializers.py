#serliazers takes the python object and conevrt ti into the json objects here 
from rest_framework.serializers import ModelSerializer
from basepage.models import Room


class Roomserializer(ModelSerializer):

    class Meta:
        model=Room
        fields="__all__"