from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.institute_course.models import Faculty
from apps.institute_course.models import Course
from apps.institute_course.models import InstituteCourse

@admin.register(InstituteCourse)
class InstituteCourseAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'institute',
    )

@admin.register(Faculty)
class FacultyAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )

@admin.register(Course)
class CourseAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )

