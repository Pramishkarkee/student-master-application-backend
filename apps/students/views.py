from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.students import serilizers, usecases
from apps.students.mixins import StudentMixin
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
        