from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.jwt import serializers, usecases
from apps.core import generics
from apps.core.mixins import LoggingErrorsMixin, ResponseMixin
from apps.user.mixins import ConsultancyUserMixin, PortalUserMixin


class NormalUserLoginView(generics.CreateAPIView, ResponseMixin):
    """
    Use this end-point to get access token for normal user
    """
    throttle_scope = 'login'

    serializer_class = serializers.NormalUserLoginSerializer
    response_serializer_class = serializers.NormalUserLoginResponseSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        pass

    @swagger_auto_schema(responses={200: serializers.NormalUserLoginResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def response(self, result, serializer, status_code):
        response_serializer = self.get_response_serializer(serializer.validated_data)
        return Response(response_serializer.data, status=status_code)


class ConsultancyUserLoginView(generics.CreateAPIView,ResponseMixin):
    """
    Use this end-point to get login for consultancy user
    """
    # message = _('Please check your email for 6 digit OTP code.')
    serializer_class = serializers.ConsultancyUserLoginSerializer
    response_serializer_class = serializers.UserIdResponseSerializer

    def perform_create(self, serializer):
        return usecases.ConsultancyUserLoginWithOTPUseCase(self.request, serializer=serializer).execute()

    @swagger_auto_schema(responses={
        200: serializers.UserIdResponseSerializer()
    })
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def response(self, serializer, result, status_code):
        serializer = self.get_response_serializer(result)
        return Response(serializer.data)


class PortalUserLoginView(ConsultancyUserLoginView):
    """
    Use this end-point to get login for portal user
    """
    pass


class CustomTokenRefreshView(LoggingErrorsMixin, TokenRefreshView):
    logging_methods = ['POST']

    serializer_class = serializers.CustomTokenRefreshSerializer


class ConsultancyUser2FAVerifyView(generics.CreateAPIView, ConsultancyUserMixin, ResponseMixin):
    serializer_class = serializers.VerifyConsultanyUserOTPSerializer
    response_serializer_class = serializers.ConsultancyUserLoginResponseSerializer

    def get_object(self):
        return self.get_consultancy_user()

    def perform_create(self, serializer):
        pass

    @swagger_auto_schema(responses={
        200: serializers.ConsultancyUserLoginResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def response(self, result, serializer, status_code):
        response_serializer = self.get_response_serializer(serializer.validated_data)
        return Response(response_serializer.data)


class PortalUser2FAVerifyView(ConsultancyUser2FAVerifyView, PortalUserMixin):

    def get_object(self):
        return self.get_portal_user()


class ResendOTPCodeView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to resend OTP code for user
    """
    message = _('Please recheck your email for 6 digit OTP code.')
    serializer_class = serializers.ResendOTPCodeSerializer

    def perform_create(self, serializer):
        return usecases.ResendOTPCodeUseCase(serializer=serializer).execute()
