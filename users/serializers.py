from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer
from django.shortcuts import render
from django.http import HttpResponse

import users.models
from users.forms import UserPhonePoleForm
from users.models import User


class UserSerializer(ModelSerializer):
    users = serializers.SerializerMethodField()

    def get_users(self, instance):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
            return User.objects.filter(invite_pole=user.invite_code)
        return []

    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(ModelSerializer):
    # users = serializers.SerializerMethodField()
    #
    # def get_users(self, instance):
    #     request = self.context.get('request')
    #     user = None
    #     if request:
    #         user = request.user
    #
    #         return User.objects.filter(invite_pole=user.invite_code)
    #     return []

    # def valid_form(self, request):
        #     if request.method == "POST":
        #         userform = UserPhonePoleForm(request.POST)
        #         if userform.is_valid():
        #             phone = userform.cleaned_data["phone"]
        #             return HttpResponse(f"<h2>Hello, {phone}</h2>")
        #         else:
        #             return HttpResponse("Invalid data")
        #     else:
        #         userform = UserPhonePoleForm()
        #         return render(request, "base.html", {"form": userform})

        # while users.objects.filter(User.invite_code == User.invite_pole).all.exists:
        #     return User.invite_pole
        # else:
        #     return HttpResponse("Неверный код приглашения")

    class Meta:
        model = User
        fields = ("users", "phone_code",)


def get_serializer_class(self):
    if self.action in ['list', 'retrieve']:
        return UserSerializer
    return UserUpdateSerializer
