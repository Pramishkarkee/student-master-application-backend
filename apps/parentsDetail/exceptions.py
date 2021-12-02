from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound, APIException


class ParentsNotFound(NotFound):
    default_detail = _('Consultancy not  found for following Id.')