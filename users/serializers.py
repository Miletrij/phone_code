from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'invite_code', 'invite_pole']


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)


class VerificationCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)


class InviteCodeSerializer(serializers.Serializer):
    invite_code = serializers.CharField(max_length=6)
