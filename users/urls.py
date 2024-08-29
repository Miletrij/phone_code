from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserProfileView, UserListView, PhoneNumberView, VerificationView

app_name = UsersConfig.name

# router = routers.DefaultRouter()
# router.register(r'users', UserUpdateAPIView, basename='users')

urlpatterns = ([
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserListView.as_view(), name='user_list'),
    path('phone/', PhoneNumberView.as_view(), name='phone'),
    path('verify/', VerificationView.as_view(), name='verify'),
    path('user/<int:user_id>/', UserProfileView.as_view(), name='profile'),

    # path("login/", auth_login_view, name="login"),
    # path("logout", LogoutView.as_view(), name="logout"),
    # path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    # path('user/update/<int:pk>', UserUpdateAPIView.as_view(), name='user_update'),
    # path('user/delete/<int:pk>', UserDestroyAPIView.as_view(), name='user_delete'),
])
# + router.urls)
