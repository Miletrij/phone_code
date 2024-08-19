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


# serializer to use when showing a list
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     model = serializers.RelatedField(many = True)
#     owner = serializers.RelatedField(many = False)
#
#     class Meta:
#         model = models.User
#
#
# # serializer to use when showing the details
# class UserUpdateSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.User

def get_serializer_class(self):
    if self.action in ['list', 'retrieve']:
        return UserSerializer
    return UserUpdateSerializer
