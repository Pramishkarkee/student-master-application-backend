from apps.parentsDetail.serializers import ParentsDetailSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.students.mixins import StudentMixin
from apps.parentsDetail import usecases



# AddParentsUseCase
class AddParentsView(generics.CreateWithMessageAPIView,StudentMixin):
    """
    Add Parents endpoint
    """
    serializer_class = ParentsDetailSerializer
    message = _("add parents successfully")

    def get_object(self):
        return self.get_student()

    def perform_create(self, serializer):
        return usecases.AddParentsUseCase(
            serializer=serializer,
            student=self.get_object()
        ).execute()