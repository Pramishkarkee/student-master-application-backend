from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny

from apps.consultancy import serializers, usecases
from apps.consultancy.mixins import ConsultancyMixin
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


class CreateConsultancyStaffView(generics.CreateWithMessageAPIView, ConsultancyMixin):
    """
    Use this end-point to create  consultancy user
    """
    message = 'Consultancy user created successfully'
    serializer_class = serializers.CreateConsultancyStaffSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        return self.get_consultancy()

    def perform_create(self, serializer):
        print(self.get_object(),self.get_consultancy())
        return usecases.CreateConsultancyStaffUseCase(
            serializer=serializer,
            consultancy=self.get_object()
        ).execute()
