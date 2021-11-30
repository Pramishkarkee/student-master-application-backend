from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.core import fields
from apps.core.models import BaseModel
from apps.core.validators import validate_image


class Academic(BaseModel):
    institute_name = models.CharField(max_length=200)
    duration = models.FloatField()
