from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny

from apps.consultancy import serializers, usecases
from apps.core import generics


class RegisterConsultancyView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to register consultancy
    """
    message = _('Registered successfully')
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterConsultancySerializer

    def perform_create(self, serializer):
        return usecases.RegisterConsultancyUseCase(
            serializer=serializer
        ).execute()
