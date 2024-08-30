import random
from string import ascii_lowercase, digits
from random import choices

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import redirect, render

from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from rest_framework import generics, request, status

from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.views import APIView

# from users.forms import UserLoginForm, UserRegisterForm
from users.models import User
from users.serializers import UserSerializer, PhoneNumberSerializer, VerificationCodeSerializer, InviteCodeSerializer

letters_and_digits = ascii_lowercase + digits


class PhoneNumberView(APIView):
    """
    Авторизация по номеру телефона, включая ввод номера,
    генерацию и отправку верификационного кода, а также перенаправление на страницу верификации.
    """
    def get(self, request):
        return render(request, 'users/phone_form.html')

    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = str(random.randint(1000, 9999))
            request.session['phone_number'] = phone_number
            request.session['verification_code'] = verification_code
            print(f'Эмуляции отправки смс-кода на номер: {phone_number}: Ваш код верификации: {verification_code}')
            return redirect('users:verify')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerificationView(APIView):
    """
    Обеспечивает процесс верификации кода, отправленного на номер телефона, включая ввод кода,
    проверку его корректности, получение или создание пользователя, а также перенаправление на страницу профиля.
    """
    def get(self, request):
        return render(request, 'users/verification_form.html')

    def post(self, request):
        serializer = VerificationCodeSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            if code == request.session.get('verification_code'):
                phone_number = request.session.get('phone_number')
                user, created = User.objects.get_or_create(phone_number=phone_number)
                return redirect('users:profile', user_id=user.id)
            return render(request, 'verification_form.html', {'error': 'Invalid code'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    """
    Обеспечивает отображение и обновление профиля пользователя, включая отображение списка пользователей,
    которые использовали его инвайт-код, а также возможность ввода и проверки инвайт-кода.
    """
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404

        users_who_used_invite_code = User.objects.filter(invite_pole=user.invite_code)
        return render(request, 'users/profile.html', {'user': user, 'users_who_used_invite_code': users_who_used_invite_code})

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = InviteCodeSerializer(data=request.data)
        if serializer.is_valid():
            invite_code = serializer.validated_data['invite_code']
            if User.objects.filter(invite_code=invite_code).exists():
                user.invite_pole = invite_code
                user.save()
                return redirect('users:profile', user_id=user.id)
            return render(request, 'users/profile.html', {'user': user, 'error': 'Invalid invite code'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(ListView):
    """
    Выводит список всех пользователей
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class HomeView(TemplateView):
    """
    Домашняя страница сайта
    """
    template_name = 'users/base.html'
