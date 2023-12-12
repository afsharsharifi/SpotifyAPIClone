from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("otp/send/", views.SendOTPToPhoneAPIView.as_view()),
    path("otp/verify/", views.VerifyOTPFromPhoneAPIView.as_view()),
    path("otp/phone/", views.VerifyPhoneUsingOTPAPIView.as_view()),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
