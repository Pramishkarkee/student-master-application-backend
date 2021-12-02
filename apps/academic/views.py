from apps.academic.mixins import AcademicMixins, EssayMixins, SopMixins
from rest_framework.serializers import Serializer
from apps.academic.serializers import CreateAcademicSerializer, CreateLorSerializer, CreateSopSerializer,CreateEssaySerializer, GetAcademicListSerializer, GetLorSerializer, GetPersonalEssay, GetSopSerializer, UpdateAcademicSerializer
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


class GetAcademicListView(generics.ListAPIView,StudentMixin):
    """
    this endpoint is use to get academic list
    """
    serializer_class = GetAcademicListSerializer
    no_content_error_message = _('no academic detail at that moment')
    def get_object(self):
        return self.get_student()

    def get_queryset(self):
        return usecases.GetAcademicListUseCase(
            student=self.get_object()
        ).execute()


class UpdateAcademicView(generics.UpdateWithMessageAPIView,AcademicMixins):
    """
    This endpoint is use to find academic list of student
    """
    serializer_class = UpdateAcademicSerializer
    parser_classes = (MultiPartParser , FileUploadParser, )
    message = _("academic detail update successfully")

    def get_object(self):
        return self.get_academic()

    def perform_update(self, serializer):
        return usecases.UpdateAcademicUseCase(
            academic=self.get_object(),
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

class GetSopView(generics.RetrieveAPIView,SopMixins):
    """
    This endpoint is use to get sop
    """
    parser_classes = (MultiPartParser , FileUploadParser, )
    serializer_class = GetSopSerializer
    no_content_error_message = _('no academic detail at that moment')
    def get_object(self):
        return self.get_sop()

    def get_queryset(self):
        return usecases.GetStudentSopUseCase(
            sop=self.get_object()
        )


class GetLorListView(generics.ListAPIView,StudentMixin):
    """
    This endpoint is use to get sudent lor
    """
    parser_classes = (MultiPartParser , FileUploadParser, )
    serializer_class = GetLorSerializer
    no_content_error_message = _('no academic detail at that moment')
    def get_object(self):
        return self.get_student()

    def get_queryset(self):
        return usecases.GetLorListUseCase(
            student=self.get_object()
        ).execute()

class GetEssayView(generics.RetrieveAPIView,EssayMixins):
    """
    This endpoint is use to get student personal essay
    """
    serializer_class = GetPersonalEssay
    def get_object(self):
        return self.get_essay()

    def get_queryset(self):
        return usecases.GetPersonalEssayUseCase(
            essay=self.get_object()
        )