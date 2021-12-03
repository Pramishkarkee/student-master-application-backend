from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound, APIException

class InstituteUserEmailNotFound(APIException):
    default_detail = _('Institute user   not  found for following email.')

class InstituteNotFound(APIException):
    default_detail = _('Institute   not  found for following id.')