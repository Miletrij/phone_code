import random

from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class UserUpdateApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        code = random.randint(1000, 9999)
        user.phone_code = f'код отправленный в смс {code}'
        user.is_active = False
        user.save()

    def perform_update(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.is_active = True
        user.save()
