from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.students import serilizers, usecases
from apps.students.mixins import AddressMixin, StudentMixin
from apps.students.models import StudentModel


# Create your views here.
class RegisterStudentView(generics.CreateWithMessageAPIView):
    """
    use this endpoind to register institute
    """
    parser_classes = (MultiPartParser, FileUploadParser,)
    message = _('Registered successfully')
    permission_classes = (AllowAny,)
    serializer_class = serilizers.RegisterStudentSerializer

    def perform_create(self, serializer):

        return usecases.RegisterStudentUseCase(
            serializer=serializer
        ).execute()


# class
class StudentInitProfileView(generics.RetrieveAPIView, StudentMixin):
    """
    Use this endpoint to get student detail
    """
    serializer_class = serilizers.StudentDetailSerializer
    def get_object(self):
        return self.get_student()

    def get_queryset(self):
        profile=usecases.GetStudentUserUseCase(
            student=self.get_object()
            ).execute()
        return profile




class UpdateStudentView(generics.UpdateWithMessageAPIView,StudentMixin):
    """
    use this endpoint to update student 
    """
    message = _("update student detail successfully")
    serializer_class = serilizers.UpdateStudentSerializer

    def get_object(self):
        return self.get_student()

    def perform_update(self, serializer):
        return usecases.UpdateStudentUseCase(
            student=self.get_student(),
            serializer = serializer
        ).execute()

class UpdateImageView(generics.UpdateWithMessageAPIView,StudentMixin):
    """
    use this endpoint to update profile
    """
    message = _("update profile is success")
    serializer_class = serilizers.UpdateProfilePictureSerializer

    def get_object(self):
        return self.get_student()

    def perform_update(self, serializer):
        return usecases.UpdateProfilePictureUseCase(
            student=self.get_student(),
            serializer = serializer
        ).execute()

class StudentAddressView(generics.CreateWithMessageAPIView,StudentMixin):
    """
    this end point is use to take student address
    """
    message =_("address complete successfully")
    permission_classes=(AllowAny,)
    serializer_class = serilizers.StudentAddressSerializer

    def get_object(self):
        return self.get_student()

    def perform_create(self, serializer):
        return usecases.AddStudentAddressUseCase(
            student_id= self.get_object(),
            serializer = serializer
        ).execute()

class StudentAddressUpdateView(generics.UpdateWithMessageAPIView,AddressMixin):
    """
    This endpoint is use to update student address
    """
    message = _("address update successfully")
    permission_classes = (AllowAny,)
    serializer_class = serilizers.StudentAddressSerializer
    def get_object(self):
        return self.get_address()

    def perform_create(self, serializer):
        return usecases.StudentAddressUpdateUseCase(
            student_id= self.get_object(),
            serializer = serializer
        ).execute()


class GetStudentAddressView(generics.RetrieveAPIView,AddressMixin):
    """
    This endpoint is use to get student address
    """
    permission_classes = (AllowAny,)
    serializer_class = serilizers.StudentAddressSerializer
    def get_object(self):
        return self.get_address()
    def get_queryset(self):
        return usecases.GetStudentAddressUseCase(
            address=self.get_queryset()
        )