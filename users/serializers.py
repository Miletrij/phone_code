from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users import models
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_code",)


def get_serializer_class(self):
    if self.action in ['list', 'retrieve']:
        return UserSerializer
    return UserUpdateSerializer
