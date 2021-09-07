from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.jwt import serializers
from apps.core import generics
from apps.core.mixins import LoggingErrorsMixin, ResponseMixin


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


class ConsultancyUserLoginView(NormalUserLoginView):
    """
    Use this end-point to get access token for consultancy user
    """
    serializer_class = serializers.ConsultancyUserLoginSerializer


class CustomTokenRefreshView(LoggingErrorsMixin, TokenRefreshView):
    logging_methods = ['POST']

    serializer_class = serializers.CustomTokenRefreshSerializer

