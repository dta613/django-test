from .models import User_list
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_list
        fields = ('username', 'password')
