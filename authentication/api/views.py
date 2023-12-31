from datetime import timedelta

from django.utils import timezone
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from extensions.utils import generate_otp
from users.models import User

from ..models import OTP
from . import serializers


class SendOTPToPhoneAPIView(APIView):
    @extend_schema(
        request=serializers.PhoneNumberSerializer,
        responses=None,
        examples=[
            OpenApiExample(
                "Example Data",
                summary="Example Data",
                value={
                    "phone": "09012345678",
                },
            ),
        ],
    )
    def post(self, request, format=None):
        serializer = serializers.PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.data["phone"]
            user = User.objects.filter(requested_phone=phone).last()
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPhoneUsingOTPAPIView(APIView):
    @extend_schema(
        request=serializers.OTPPhoneNumberSerializer,
        responses=None,
        examples=[
            OpenApiExample(
                "Example Data",
                summary="Example Data",
                value={"phone": "09012345678", "otp_code": "123456"},
            )
        ],
    )
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
                user = User.objects.filter(requested_phone=phone).last()
                user.is_active = True
                user.verified_phone = user.requested_phone
                user.save()
                User.objects.filter(requested_phone=phone, is_active=False).delete()
                return Response({"detail": "شماره تلفن با موفقیت تایید شد"}, status=status.HTTP_200_OK)
            return Response({"detail": "کد یکبار مصرف اشتباه است"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateAPIView(CreateAPIView):
    model = User
    serializer_class = serializers.UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        requested_phone = request.data.get("requested_phone")
        user = User.objects.filter(verified_phone=requested_phone).first()
        if user:
            return Response({"detail": "این شماره تلفن قبلا تایید شده است"}, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=None, responses=serializers.UserRegisterSerializer)
    def get(self, request, format=None):
        user = User.objects.get(id=request.user.id)
        serializer = serializers.UserRegisterSerializer(user)
        return Response(serializer.data)
