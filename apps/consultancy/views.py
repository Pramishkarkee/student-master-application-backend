from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.permissions import AllowAny

from apps.consultancy import serializers, usecases
from apps.consultancy.mixins import ConsultancyMixin, ConsultancyStaffMixin
from apps.core import generics
from apps.user.mixins import ConsultancyUserMixin


class RegisterConsultancyView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to register consultancy
    """
    parser_classes = (MultiPartParser,FileUploadParser,)
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
    message = 'Consultancy staff created successfully'
    serializer_class = serializers.CreateConsultancyStaffSerializer
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FileUploadParser,)

    def get_object(self):
        return self.get_consultancy()

    def perform_create(self, serializer):
        return usecases.CreateConsultancyStaffUseCase(
            serializer=serializer,
            consultancy=self.get_object()
        ).execute()


class CreatePasswordForConsultancyUserView(generics.CreateWithMessageAPIView, ConsultancyUserMixin):
    """
    Use this endpoint to save password of consultancy user
    """
    message = 'Password saved successfully.'
    serializer_class = serializers.CreatePasswordForConsultancyStaffSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        return self.get_consultancy_user()

    def perform_create(self, serializer):
        return usecases.CreatePasswordForConsultancyUserUseCase(
            serializer=serializer,
            consultancy_user=self.get_object()
        ).execute()


class ListConsultancyStaffView(generics.ListAPIView, ConsultancyMixin):
    """
    Use this endpoint to list all staff of particular consultancy
    """
    serializer_class = serializers.ListConsultancyStaffSerializer

    def get_object(self):
        return self.get_consultancy()

    def get_queryset(self):
        return usecases.ListConsultancyStaffUseCase(consultancy=self.get_object()).execute()


class ListConsultancyView(generics.ListAPIView):
    serializer_class = serializers.ListConsultancySerializer

    def get_queryset(self):
        return usecases.ListConsultancyUseCase().execute()


class UpdateConsultancyStaffView(generics.UpdateWithMessageAPIView, ConsultancyStaffMixin):
    """
    Use this end point to update consultancy staff details
    """

    serializer_class = serializers.UpdateConsultancyStaffSerializer

    def get_object(self):
        return self.get_consultancy_staff()

    def perform_update(self, serializer):
        return usecases.UpdateConsultancyStaffUseCase(
            serializer=serializer,
            consultancy_staff=self.get_object()
        ).execute()
