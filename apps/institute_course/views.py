from apps import institute
from apps.auth.jwt import serializers
from apps.institute_course.mixins import ApplyMixin, CourseMixin, FacultyMixin
from apps.institute.mixins import InstituteMixins
from apps.institute_course import usecases
from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.institute_course.serializers import (
    CancleStudentApplicationSerializer,
    CommentApplicationSerializer,
    CourseSerializer, 
    FacultySerializer,
    GetStudentApplicantSerializer,
    GetStudentApplicationInstituteSerializer, 
    InstituteCourseSerializer,
    AddInstituteCourseSerializer,
    ListApplicationCommentSerializer, 
    ListInstituteCourseSerializer, 
    StudentApplySerializer)

from apps.students.mixins import StudentMixin
from apps.institute_course import usecases
# from apps.institute_course.mixins import InstituteCourseMixin

class AddInstituteCourse(generics.CreateWithMessageAPIView,InstituteMixins):
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

class ListInstituteCourse(generics.ListAPIView,InstituteMixins):
    """
    this end point is use to list course 
    put institute id in institute_id field
    """
    serializer_class = ListInstituteCourseSerializer
    permission_classes = (AllowAny,)
    no_content_error_message = _("No Consultancy staff at the moment.")
    def get_object(self):
        return self.get_institute()

    def get_queryset(self):
        return usecases.GetInstituteCourseUseCase(
            inst=self.get_object()
        ).execute()


class UpdateInstituteCourse(generics.UpdateWithMessageAPIView,CourseMixin):
    """
    This endpoint is use to update institute course
    """

    serializer_class = AddInstituteCourseSerializer
    permission_classes = (AllowAny,)
    message = _("update successfully")

    def get_object(self):
        return self.get_institutecourse()

    def perform_update(self, serializer):
        return usecases.UpdateInstituteCourseUseCase(
            institute_course=self.get_object(),
            serializer = serializer
        ).execute()



class DeleteInstituteCourseView(generics.DestroyWithMessageAPIView,CourseMixin):
    """
    This endpoint is use to destroy institute course
    """
    message = _("institute course delete successfully")

    def get_object(self):
        return self.get_institutecourse()

    def perform_destroy(self, instance):
        return usecases.DeleteInstituteCourseUseCase(
            institute_course= self.get_object()
        ).execute()


class ListFacultyView(generics.ListAPIView):
    """
    This endpoint is use to list faculty
    """
    serializer_class = FacultySerializer

    def get_queryset(self):
        return usecases.ListFacultyUseCase().execute()

class ListCourseView(generics.ListAPIView,FacultyMixin):
    """
    This end point is use to get course
    """
    serializer_class = CourseSerializer

    def get_object(self):
        return self.get_faculty()

    def get_queryset(self):
        return usecases.ListCourseUseCase(
            faculty= self.get_object()
        ).execute()

class ApplyInstituteCourseView(generics.CreateWithMessageAPIView):
    """
    This endpoint is use to apply
    """
    serializer_class = StudentApplySerializer
    message = _("student apply successfully")
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        return usecases.ApplyUseCase(
            serializer = serializer
        ).execute()

class AddCommentApplicationView(generics.CreateWithMessageAPIView,ApplyMixin):
    """
    This api is use to comment on student application
    """
    serializer_class = CommentApplicationSerializer
    message = "comment successfully"

    def get_object(self):
        return self.get_apply()

    def perform_create(self, serializer):
        return usecases.AddCommentApplyInstitute(
            serializer =serializer,
            apply = self.get_object()
        )

class GetListCommentApplicationView(generics.ListAPIView,ApplyMixin):
    """
    this endpoint is use to get comment
    """
    serializer_class = ListApplicationCommentSerializer

    def get_object(self):
        return self.get_apply()

    def get_queryset(self):
        return usecases.ListCommentInstituteUseCase(
            apply = self.get_object()
        ).execute()

class ListStudentApplicationView(generics.ListAPIView,InstituteMixins):
    """
    this api is use to list application
    """
    serializer_class = GetStudentApplicationInstituteSerializer
    def get_object(self):
        return self.get_institute()

    def get_queryset(self):
        return usecases.ListStudentApplicationCourseUseCase(
            institute=self.get_object()
        ).execute()


class CancleStudentApplication(generics.UpdateWithMessageAPIView,ApplyMixin):
    """
    This endpoint is use to cancle application
    """
    serializer_class = CancleStudentApplicationSerializer
    def get_object(self):
        return self.get_apply()

    def perform_update(self, serializer):
        return usecases.CancleStudentApplicationUseCase(
            application=self.get_object(),
            serializer = serializer
        ).execute()


