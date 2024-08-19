import random

from rest_framework import viewsets

from users import models, serializers
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


# class DualSerializerViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet providing different serializers for list and detail views.
#
#     Use list_serializer and detail_serializer to provide them
#     """
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return serializers.UserSerializer
#         if self.action == 'retrieve':
#             return serializers.UserUpdateSerializer
#         return serializers.User
#
#
# class UserViewSerializer(UserUpdateApiView):
#     model = models.User
#     list_serializer = serializers.UserSerializer
#     detail_serializer = serializers.UserUpdateSerializer


