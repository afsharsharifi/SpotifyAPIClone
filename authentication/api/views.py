from datetime import timedelta

from django.shortcuts import get_object_or_404
from django.utils import timezone
from extensions.utils import generate_otp
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from users.models import User
from drf_spectacular.utils import extend_schema

from ..models import OTP
from . import serializers


class SendOTPToPhoneAPIView(APIView):
    @extend_schema(request=serializers.PhoneNumberSerializer)
    def post(self, request, format=None):
        serializer = serializers.PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.data["phone"]
            otp_code = generate_otp()
            obj, created = OTP.objects.update_or_create(
                phone=phone,
                defaults={"otp_code": otp_code, "expire_at": timezone.now() + timedelta(seconds=150)},
            )
            # ! Action to Send OTP to Phone Strats
            print(f"OTP for {phone} is >>>>>>>>> {otp_code}")
            # ! Action to Send OTP to Phone Ends
            return Response(
                {
                    "detail": f"کد با موفقیت یرای {phone} ارسال شد",
                    "code": f"کد {otp_code} میباشد صرفا جهت تست",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )


class VerifyOTPFromPhoneAPIView(APIView):
    @extend_schema(request=serializers.OTPPhoneNumberSerializer)
    def post(self, request, format=None):
        serializer = serializers.OTPPhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.data["phone"]
            otp_code = serializer.data["otp_code"]
            if not OTP.objects.filter(phone=phone):
                return Response({"detail": "برای این شماره تلفن کدی وجود ندارد"}, status=status.HTTP_404_NOT_FOUND)
            otp_obj = OTP.objects.get(phone=phone)
            if otp_obj.otp_code == otp_code:
                if otp_obj.expire_at < timezone.now():
                    return Response({"detail": "کد یکبار مصرف منقضی شده است"}, status=status.HTTP_408_REQUEST_TIMEOUT)
                return Response({"detail": "کد یکبار مصرف صحیح است"}, status=status.HTTP_200_OK)
            return Response({"detail": "کد یکبار مصرف اشتباه است"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPhoneUsingOTPAPIView(APIView):
    @extend_schema(request=serializers.OTPPhoneNumberSerializer)
    def post(self, request, format=None):
        serializer = serializers.OTPPhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.data["phone"]
            otp_code = serializer.data["otp_code"]
            if not OTP.objects.filter(phone=phone):
                return Response({"detail": "برای این شماره تلفن کدی وجود ندارد"}, status=status.HTTP_404_NOT_FOUND)
            otp_obj = OTP.objects.get(phone=phone)
            if otp_obj.otp_code == otp_code:
                if otp_obj.expire_at < timezone.now():
                    return Response({"detail": "کد یکبار مصرف منقضی شده است"}, status=status.HTTP_408_REQUEST_TIMEOUT)
                user = get_object_or_404(User, phone=phone)
                user.is_active = True
                user.save()
                return Response({"detail": "شماره تلفن با موفقیت تایید شد"}, status=status.HTTP_200_OK)
            return Response({"detail": "کد یکبار مصرف اشتباه است"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateAPIView(CreateAPIView):
    model = User
    serializer_class = serializers.UserRegisterSerializer
