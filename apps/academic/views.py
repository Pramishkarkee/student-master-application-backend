from rest_framework.serializers import Serializer
from apps.academic.serializers import CreateAcademicSerializer, CreateLorSerializer, CreateSopSerializer,CreateEssaySerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.students.mixins import StudentMixin
from apps.students import mixins
from apps.academic import usecases
# Create your views here.

class CreateAcademicView(generics.CreateWithMessageAPIView,StudentMixin):
    """
    use this endpoint to add academic detail
    """
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FileUploadParser,)
    serializer_class = CreateAcademicSerializer
    message = _("Academic Detail added successfully")

    def get_object(self):
        return self.get_student()

    def perform_create(self, serializer):
        return usecases.CreateStudentAcademicUseCase(
            student=self.get_object(),
            serializer=serializer
        ).execute()

class CreateSopView(generics.CreateWithMessageAPIView,StudentMixin):
    """
    use this endpoint to add sop one student can add one sop
    """
    permission_classes = (AllowAny ,)
    parser_classes = (MultiPartParser , FileUploadParser, )
    serializer_class = CreateSopSerializer
    message = _("SOP Add successfully")

    def get_object(self):
        return self.get_student()

    def perform_create(self, serializer):
        return usecases.CreateStudentSopUseCase(
            student = self.get_object(),
            serializer =serializer
        ).execute()


class CreateLorView(generics.CreateWithMessageAPIView,StudentMixin):
    """
    use this endpoint to add lor ons student can add more then one lor
    """
    permission_classes = (AllowAny ,)
    parser_classes = (MultiPartParser , FileUploadParser, )
    serializer_class = CreateLorSerializer
    message = _("Lor Add successfully")

    def get_object(self):
        return self.get_student()

    def perform_create(self, serializer):
        return usecases.CreateStudentLorUseCase(
            student = self.get_object(),
            serializer =serializer
        ).execute()

class CreatePersonalEssayView(generics.CreateWithMessageAPIView,StudentMixin):
    """
    use this endpoint to add student personal essay one student can add one essay
    """
    permission_classes = (AllowAny ,)
    parser_classes = (MultiPartParser , FileUploadParser, )
    serializer_class = CreateEssaySerializer
    message = _("personal essay Add successfully ")
    def get_object(self):
        return self.get_student()

    def perform_create(self, serializer):
        return usecases.CreateStudentEssayUseCase(
            student = self.get_object(),
            serializer =serializer
        ).execute()