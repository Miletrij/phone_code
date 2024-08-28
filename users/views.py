import random
from string import ascii_lowercase, digits
from random import choices

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from rest_framework import generics, request

from django.contrib.auth import login

from users.forms import UserLoginForm, UserRegisterForm
from users.models import User
from users.serializers import UserSerializer

letters_and_digits = ascii_lowercase + digits


class UserCreateAPIView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users/login.html')

    def form_valid(self, form):
        recipient = form.save()
        recipient.owner = self.request.user
        recipient.save()
        return super().form_valid(form)

# class UserCreateAPIView(LoginRequiredMixin, CreateView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     fields = ("phone", "phone_code",)
#
#     def perform_create(self, serializer):
#         user = serializer.save()
#         # user.set_password(user.password)
#         auth_code = random.randint(1000, 9999)
#         user.phone_code = "Код отправленный в смс: " + str(auth_code)
#         user.is_active = False
#         user.save()
#
#     def perform_update(self, serializer):
#         user = serializer.save()
#         # user.set_password(user.password)
#         # invite_code = ''.join(choices(letters_and_digits, k=6))
#         # user.invite_code = invite_code
#         user.is_active = True
#         user.save()


class UserListAPIView(ListView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(DetailView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_success_url(self):
        return reverse_lazy('user:user_list', kwargs={'pk': self.get_object().id})


class UserDestroyAPIView(DeleteView):
    queryset = User.objects.all()


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    # success_url = reverse_lazy("users:index")

    def get_success_url(self):
        # return reverse("users/index.html")
        return redirect('/')


def auth_login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get("phone")
            phone_code = form.cleaned_data.get("phone_code")
            user = User.objects.filter(phone=phone, phone_code=phone_code).first()
            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error("phone", "пользователь не найден!!!")
            # elif:
            #     form.add_error("phone_code", "код авторизации не совпадает!!!")
            #     "дописать форму else при отсутствии пользователя и неправильном пароле + отправка на страницу регистрации"
    else:
        form = UserLoginForm()

    return render(request, "users/login.html", {"form": form})


class HomeView(TemplateView):
    template_name = 'users/index.html'


class UserPoleAPIView(ListView):
    template_name = 'users/invite_code.html'
    serializer_class = UserSerializer
    queryset = User.objects.filter(invite_pole="invite_pole")

    class Meta:
        model = User
        fields = ("invite_pole",)
