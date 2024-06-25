from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
  # User creation
  path("register/", UserRegistrationAPIView.as_view(), name="register-user"),
  path("login/", UserLoginAPIView.as_view(), name="Login-user"),
  path("logout/", UserLogoutAPIView.as_view(), name="Logout-user"),
  path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
  path("user/", UserInfoAPIView.as_view(), name="user-info"),

  # Post Creation

]