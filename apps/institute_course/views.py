from apps.institute_course import usecases
from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.institute_course.serializers import InstituteCourseSerializer,AddInstituteCourseSerializer
from apps.institute_course import usecases
from apps.institute_course.mixins import InstituteCourseMixin

class AddInstituteCourse(generics.CreateWithMessageAPIView,InstituteCourseMixin):
    """
    Use this endpoint to add course
    """
    message = _('Create successfully')
    serializer_class = AddInstituteCourseSerializer
    permission_classes = (AllowAny,)
    
    def get_object(self):
        return self.get_institute()
    def perform_create(self, serializer):
        return usecases.AddCourseUseCase(
            serializer = serializer,
            institute = self.get_object()
             ).execute()

# class ListInstituteCourse(generics.ListAPIView):
    # """
    # this end point is use to list course 
    # put institute id in institute_id field
    # """






