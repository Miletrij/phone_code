from django.contrib.auth.forms import AuthenticationForm
from common.views import StyleFormMixin

from users.models import User


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ("phone", "phone_code")
