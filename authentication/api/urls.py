from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("register/", views.UserCreateAPIView.as_view()),
    path("otp/send/", views.SendOTPToPhoneAPIView.as_view()),
    path("otp/check/", views.VerifyPhoneUsingOTPAPIView.as_view()),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
