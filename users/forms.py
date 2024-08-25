from django.contrib.auth.forms import AuthenticationForm
from django import forms

from common.views import StyleFormMixin

from users.models import User


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите имя пользователя"}))
    phone_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите код"}))


    class Meta:
        model = User
        fields = ("phone", "phone_code")


class UserPhonePoleForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ("phone_pole",)
