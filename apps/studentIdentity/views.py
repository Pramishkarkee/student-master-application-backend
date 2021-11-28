from apps.students.mixins import StudentMixin
from apps.studentIdentity.serializers import StudentCitizenshipSerializer
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