from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.consultancy.utils import upload_consultancy_logo_to, upload_consultancy_cover_image_to, \
    upload_consultancy_staff_image_to
from apps.core import fields
from apps.core.models import BaseModel
from apps.core.validators import validate_image
from apps.staff.models import StaffPosition
from apps.user.models import ConsultancyUser


class Consultancy(BaseModel):
    name = models.CharField(max_length=250)
    contact = fields.PhoneNumberField()
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    website = models.URLField()
    logo = models.ImageField(
        upload_to=upload_consultancy_logo_to,
        default='consultancy/logo/default_logo.png',
        validators=[validate_image]
    )
    cover_image = models.ImageField(
        upload_to=upload_consultancy_cover_image_to,
        default='consultancy/cover_image/default_cover_image.png',
        validators=[validate_image]
    )
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ConsultancyStaff(BaseModel):
    user = models.OneToOneField(ConsultancyUser, on_delete=models.CASCADE)
    consultancy = models.ForeignKey(Consultancy, on_delete=models.CASCADE)
    role = models.ForeignKey(StaffPosition, on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        upload_to=upload_consultancy_staff_image_to,
        default='consultancy_staff/photo/default_logo.png',
        validators=[validate_image]
    )

    @property
    def get_consultancy_user_email(self):
        return self.user.email

    @property
    def get_consultancy_full_name(self):
        return self.user.fullname

    def __str__(self):
        return self.user.email

    def clean(self):
        if self.role.name == 'owner' and StaffPosition.objects.filter(
                name__iexact='owner',
        ).exists():
            raise DjangoValidationError(
                {'role': _('Cannot Assign two owners.')}
            )
