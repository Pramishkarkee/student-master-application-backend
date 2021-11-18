from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.students.utils import upload_student_image_to
from apps.core import fields
from apps.core.models import BaseModel
from apps.core.validators import validate_image
from apps.user.models import StudentUser


# Create your models here.
class StudentModel(BaseModel):
    user = models.OneToOneField(StudentUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    contact = fields.PhoneNumberField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(
        upload_to=upload_student_image_to,
        default='student/image/default_logo.png',
        validators=[validate_image]
    )

    def __str__(self):
        return self.name


class TemporaryAddress(BaseModel):
    student = models.OneToOneField(StudentModel, on_delete=models.CASCADE)
    state_provision = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.country


class PermanentAddress(BaseModel):
    student = models.OneToOneField(StudentModel, on_delete=models.CASCADE)
    state_provision = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.country
