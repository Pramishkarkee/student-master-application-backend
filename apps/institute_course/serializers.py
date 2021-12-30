import re

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.institute_course import models
from rest_framework.validators import UniqueTogetherValidator

from apps.institute_course.models import CommentApplicationInstitute, Course, Faculty, InstituteApply, InstituteCourse
from apps.core import fields
from apps.students.models import StudentModel,StudentAddress


User = get_user_model()

class InstituteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteCourse
        fields = '__all__'
        # validators = [UniqueTogetherValidator(
        #     queryset=InstituteCourse.objects.all(),
        #     fields=['institute','course']
        # )]

class AddInstituteCourseSerializer(InstituteCourseSerializer):
    class Meta(InstituteCourseSerializer.Meta):
        fields = (
            'program',
            'faculty',
            'course',
            'intake',
            'eligibility',
            'score',
            'last_mini_academic_score',
            'duration_year',
            'total_fee',
            'fee_currency',
            'reg_status',
            'reg_open',
            'reg_close'
        )

        # validators = [UniqueTogetherValidator(
        #     queryset=InstituteCourse.objects.all(),
        #     fields=['institute','course']
        # )]
    # def validate(self, attrs):
    #     attrs = super().validate(attrs)

    #     if "institute" in attrs and "course" in attrs:
    #         try:
    #             self.institute = InstituteCourse.objects.get(institute=attrs['institute'],course=attrs['course'])
            
    #         except InstituteCourse.DoesNotExist:

    #             pass

    #         del attrs['id']
    #     return attrs

    # def create(self, validate_data):
    #     return InstituteCourse.objects.get_or_create(**validate_data)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'description'
        )

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = (
            'name',
            'id'
        )


class ListInstituteCourseSerializer(InstituteCourseSerializer):

    course = CourseSerializer(read_only =True)
    faculty =FacultySerializer(read_only = True)
    class Meta(InstituteCourseSerializer.Meta):
        fields = (
            'id',
            'program',
            'faculty',
            'course',
            'intake',
            'eligibility',
            'score',
            'last_mini_academic_score',
            'duration_year',
            'total_fee',
            'fee_currency',
            'reg_status',
            'reg_open',
            'reg_close'
        )

    
class CommentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentApplicationInstitute
        fields = (
            'institute_user',
            'comment'
        )

class ListApplicationCommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="commentor_name")

    class Meta:
        model = CommentApplicationInstitute
        fields = (
            'name',
            'created_at',
            'comment'
        )
class StudentApplySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InstituteApply
        fields = (
            'student',
            'course',
            'institute',
            'consultancy'
        )


class GetStudentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAddress
        fields = ['state_provision','country']

class GetStudentApplicantSerializer(serializers.ModelSerializer):
    address_relation=GetStudentAddressSerializer(many=False,read_only =True)
    class Meta:
        model = StudentModel
        fields = (
            'fullname',
            'address_relation'
            )

class ApplicationInstituteCourseSerializer(InstituteCourseSerializer):

    course = CourseSerializer(read_only =True)
    class Meta(InstituteCourseSerializer.Meta):
        fields = (
            'course',
        )

# class GetStudentApplicationInstituteSerializer(serializers.ModelSerializer):
#     student = GetStudentApplicantSerializer(many=False,read_only =True)
#     course = ApplicationInstituteCourseSerializer(many=False,read_only =True)
#     # consultancy = serializers.CharField()

#     class Meta:
#         model = InstituteApply
#         fields = (
#             'student',
#             'course',
#             'consultancy',
#             'action',
#             'cancel',
#             'created_at'
#         )

class CancleStudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteApply
        fields = (
            'cancel',
        )


class GetStudentApplicationInstituteSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='get_student_user_name')
    consultancy = serializers.CharField(source='get_consultancy_name')
    course = serializers.CharField(source='get_student_course') 
    address = serializers.CharField(source='student_address')
    class Meta:
        model = InstituteApply
        fields = (
            'id',
            'student',
            'student_name',
            'course',
            'consultancy',
            'action',
            'cancel',
            'created_at',
            'address',
        )