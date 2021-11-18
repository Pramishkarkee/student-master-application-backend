from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound, APIException


class StudentModelNotFound(NotFound):
    default_detail = _('Student Not Found for following Id')
