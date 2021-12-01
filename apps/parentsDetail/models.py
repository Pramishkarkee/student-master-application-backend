from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.db.models import Q
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _

from apps.core import fields
from apps.core.models import BaseModel
from apps.students.models import StudentModel

class StudentParents(BaseModel):
    RELATION_CHOICE = (
        ('father','father'),
        ('mother','mother')
    )
    student = models.ForeignKey(StudentModel , on_delete=CASCADE)
    relation = models.CharField(choices=RELATION_CHOICE,max_length=20)
    fullname = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    annual_income = models.FloatField(blank=True,default=0.0) #defauly should be in dollor
    currency = models.CharField(default="USD",max_length=50)

    class Meta:
        unique_together = ('student','relation')
