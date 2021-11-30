from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.db.models import Q
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator ,MinValueValidator
from rest_framework.validators import UniqueValidator

from apps.core import fields
from apps.core.models import BaseModel
from apps.core.validators import validate_image
from apps.students.models import StudentModel
from django.db.models.signals import pre_save
from apps.academic.utils import check_score,upload_academic_doc_to

class Academic(BaseModel):
    LEVEL_CHOICE=(
        ('school','school'),
        ('high_school','high_school'),
        ('undergraduate','undergraduate'),
        ('graduate','graduate'),
        ('post_graduate','post_graduate')
    )
    student = models.ForeignKey(StudentModel ,on_delete=CASCADE)
    institute_name = models.CharField(max_length=200)
    duration = models.FloatField(
        validators=[MinValueValidator(0.0),MaxValueValidator(15.0)],
        blank=True
    )
    level = models.CharField(max_length=200,choices=LEVEL_CHOICE)
    score = models.FloatField()
    full_score=models.FloatField(
        validators=[MinValueValidator(0.0),MaxValueValidator(100.0)],
    )
    marksheet = models.FileField(
        upload_to=upload_academic_doc_to,
    )
    certificate = models.FileField(
        upload_to=upload_academic_doc_to,
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student','level'],name='student academic')
        ]


        
pre_save.connect(check_score, sender=Academic)
