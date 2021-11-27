from datetime import datetime
from django.core import validators
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models

from apps.institute.utils import past_date,upload_institute_staff_image_to,upload_institute_logo_to,upload_institute_cover_image_to
from apps.core import fields
from apps.core.models import BaseModel
from apps.core.validators import validate_image
from apps.staff.models import StaffPosition
from apps.user.models import InstituteUser
# from apps.institute_course.models import InstituteCourse


# Create your models here.
class Institute(BaseModel):
    name = models.CharField(max_length=250)
    contact = fields.PhoneNumberField()
    category = models.CharField(max_length=200)   #this represemt college or university
    university = models.CharField(max_length=200, blank=True) #if catagory is college then add university name else not required
    established = models.DateField(
        default=datetime.now,
        validators= [past_date]
         )
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    website = models.URLField()
    logo = models.ImageField(
        upload_to=upload_institute_logo_to,
        default='institute/logo/default_logo.png',
        validators=[validate_image]
    )
    cover_image = models.ImageField(
        upload_to=upload_institute_cover_image_to,
        default='institute/cover_image/default_cover_image.png',
        validators=[validate_image]
    )
    # about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class InstituteStaff(BaseModel):
    user = models.OneToOneField(InstituteUser, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    role = models.ForeignKey(StaffPosition, on_delete=models.CASCADE)
    profile_photo= models.ImageField(
        upload_to=upload_institute_staff_image_to,
        default="institute_staff/photo/default_logo.png",
        validators=[validate_image]
    )

    @property
    def get_institute_user_email(self):
        return self.user.email 

    @property
    def get_institute_full_name(self):
        return self.user.fulname

    def __self__(self):
        return self.user.email 

    def clean(self):
        if self.role.name == 'owner' and StaffPosition.objects.filter(
            name__iexact='owner',
        ).exists():
            raise DjangoValidationError(
                {
                    'role':_('Cannot Assign two owners. ')
                }
            )

# class Course

# class InstituteDetailForm

class RequiredDocument(BaseModel):
    photo = models.BooleanField()
    citizenship = models.BooleanField()
    passport = models.BooleanField()
    academic_certificate = models.BooleanField()
    sop = models.BooleanField()
    lor = models.BooleanField()

class ScholorshipScheme(BaseModel):
    topic = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        self.topic

# class ScholorshipSchemeCourse(BaseModel):
#     scholorship = models.ForeignKey(ScholorshipScheme, on_delete=models.CASCADE)
#     course = models.ForeignKey(InstituteCourse , on_delete=models.CASCADE)