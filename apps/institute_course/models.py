from django.core import validators
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.db.models import Q
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator,MinValueValidator
from apps.institute.models import Institute, InstituteScholorship
import datetime

from apps.core import fields
from apps.core.models import BaseModel
# Create your models here.

class Faculty(BaseModel):
    name = models.CharField(max_length=200)

class Course(BaseModel):
    faculty=models.ForeignKey(Faculty , on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.TextField()

class InstituteCourse(BaseModel):
    INTAKE_CHOICE=(
        ('spring' , 'spring'),
        ('yearly' , 'yearly'),
        ('fall' , 'fall' )
    )
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    program=models.CharField(max_length=200)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    intake=models.CharField(max_length=100,choices=INTAKE_CHOICE)
    #relete the eligibility exam in next table 
    eligibility = models.CharField(max_length=200)
    score = models.FloatField()
    last_mini_academic_score = models.FloatField(
        validators=[MinValueValidator(40.0),MaxValueValidator(100.0)]
        )
    duration_year = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)]
    ) 
    total_fee = models.DecimalField(max_digits=10, decimal_places=3)
    fee_currency = models.CharField(max_length=20)

    #this all are form open and close field

    reg_status = models.BooleanField(default=True)
    reg_open = models.DateField(
        _("Date"),
        blank=True
        )

    reg_close = models.DateField(
        _("Date"),
        blank=True
    )
    
    class Meta:
        unique_together = ('course','institute')

# class ScholorshipLinkCourse(BaseModel):
#     scholorship = models.ForeignKey(InstituteScholorship, on_delete=models.CASCADE)
#     course = models.ForeignKey(InstituteCourse, on_delete=models.CASCADE)

