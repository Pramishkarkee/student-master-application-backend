from django.shortcuts import render


# Create your views here.
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.portal import serializers, usecases


class RegisterPortalView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to register consultancy
    """
    message = _('Registered successfully')
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterPortalSerializer

    def perform_create(self, serializer):
        return usecases.RegisterConsultancyUseCase(
            serializer=serializer
        ).execute()
