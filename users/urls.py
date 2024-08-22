from django.urls import path
from rest_framework import routers
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserCreateAPIView, UserRetrieveAPIView, UserListAPIView, UserDestroyAPIView, \
    UserLoginView

app_name = UsersConfig.name

# router = routers.DefaultRouter()
# router.register(r'users', UserUpdateAPIView, basename='users')

urlpatterns = ([
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", UserLoginView.as_view(), name="login"),
    path('user/', UserListAPIView.as_view(), name='user_list'),
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('user/update/<int:pk>', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>', UserDestroyAPIView.as_view(), name='user_delete'),

])
# + router.urls)
