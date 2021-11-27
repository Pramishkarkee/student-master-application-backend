from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound, APIException

class InstituteNotFound(NotFound):
    default_detail = _('institute not found')

class CourseNotFound(NotFound):
    default_detail = _('course not found')

class FacultyNotFound(NotFound):
    default_detail = _('faculty not found')