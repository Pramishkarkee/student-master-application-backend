import re

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.institute_course import models
from rest_framework.validators import UniqueTogetherValidator

from apps.institute_course.models import Course, Faculty, InstituteApply, InstituteCourse
from apps.core import fields

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

    
# class StudentApplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Faculty,
#         fields = '__all__'
class StudentApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteApply
        fields = (
            'student',
            'course',
            'institute',
            'consultancy'
        )