import random
from string import ascii_lowercase, digits
from random import choices

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from rest_framework import generics, request


from users.forms import UserLoginForm
from users.models import User
from users.serializers import UserSerializer

letters_and_digits = ascii_lowercase + digits


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        # user.set_password(user.password)
        auth_code = random.randint(1000, 9999)
        user.phone_code = "Код отправленный в смс: " + str(auth_code)
        user.is_active = False
        user.save()

    def perform_update(self, serializer):
        user = serializer.save()
        # user.set_password(user.password)
        invite_code = ''.join(choices(letters_and_digits, k=6))
        user.invite_code = invite_code
        user.is_active = True
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    # success_url = reverse_lazy("users:index")

    def get_success_url(self):
        # return reverse("users/index.html")
        return redirect('/')

class HomeView(TemplateView):
    template_name = 'users/index.html'


