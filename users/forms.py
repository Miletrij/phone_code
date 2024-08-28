from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from common.views import StyleFormMixin

from users.models import User


# class UserLoginForm(StyleFormMixin, AuthenticationForm):
#     phone = forms.CharField(widget=forms.TextInput(attrs={
#         'class': "form-control py-4",
#         'placeholder': "Введите имя пользователя"}))
#     phone_code = forms.CharField(widget=forms.TextInput(attrs={
#         'class': "form-control py-4",
#         'placeholder': "Введите код"}))
#
#
#     class Meta:
#         model = User
#         fields = ("phone", "phone_code")


class UserPhonePoleForm(StyleFormMixin):
    class Meta:
        model = User
        fields = ("phone_pole",)


class UserLoginForm(StyleFormMixin, forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите телефон пользователя"}))
    phone_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите код"}))

    class Meta:
        model = User
        fields = ("phone", "phone_code")


class UserRegisterForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ("phone", "phone_code")
