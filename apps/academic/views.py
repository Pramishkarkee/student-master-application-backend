from apps.academic.serializers import CreateAcademicSerializer
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
