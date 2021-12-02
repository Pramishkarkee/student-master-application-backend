from apps.studentIdentity.mixins import CitizenshipMixins, PassportMixins
from rest_framework import serializers
from apps.students.mixins import StudentMixin
from apps.studentIdentity.serializers import GetCitizenshipSerializer, GetPassportSerializer, StudentCitizenshipSerializer, StudentPassportSerializer
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from apps.studentIdentity import usecases
from apps.core import generics

# Create your views here.

class AddCitizenshipView(generics.CreateWithMessageAPIView , StudentMixin):
    serializer_class = StudentCitizenshipSerializer
    message = _("add citizenship successfully")

    def get_object(self):
        return self.get_student()


    def perform_create(self, serializer):
        return usecases.AddCitizenshipUseCase(
            serializer = serializer,
            student_id = self.get_object()
        ).execute()

class AddPassportView(generics.CreateWithMessageAPIView,StudentMixin):
    """
    Add passport endpoint
    """
    serializer_class = StudentPassportSerializer
    message = _("add passport successfully")

    def get_object(self):
        return self.get_student()

    def perform_create(self, serializer):
        return usecases.AddPassportUseCase(
            serializer=serializer,
            student_id=self.get_object()
        ).execute()
        

class GetCitizenshipView(generics.RetrieveAPIView,CitizenshipMixins):
    """
    this endpoint is use to find student citizenship
    """
    serializer_class =GetCitizenshipSerializer
    def get_object(self):
        return self.get_citizenship()

    def get_queryset(self):
        return usecases.GetStudentCitizenshipUseCase(
            citizenship=self.get_object()
        ).execute()

class GetPassportView(generics.RetrieveAPIView,PassportMixins):
    """
    this endpoint is use to find student citizenship
    """
    serializer_class = GetPassportSerializer
    def get_object(self):
        return self.get_passport()

    def get_queryset(self):
        return usecases.GetStudentPassportUseCase(
            passport=self.get_object()
        ).execute()