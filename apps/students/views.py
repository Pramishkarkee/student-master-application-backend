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
    def get_queryset(self):
        # print("*************************************************",self.request._student)
        profile=usecases.GetStudentUserUseCase(student=self.kwargs.get('student_id')).execute()
        print("&&&&&&&&&&&&&&&",profile)
        return profile
