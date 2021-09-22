from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.core.exceptions import ValidationError as DjangoValidationError

from apps.core import fields
from apps.core.models import BaseModel
from apps.core.validators import validate_image
from apps.portal.utils import upload_portal_user_cover_image_to
from apps.staff.models import StaffPosition
from apps.user.models import PortalUser


class Portal(BaseModel):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    profile_picture = models.ImageField(
        upload_to=upload_portal_user_cover_image_to,
        default='portal/profile/default_profile_picture.png',
        validators=[validate_image]
    )

    def __str__(self):
        return self.name


class PortalStaff(BaseModel):
    user = models.OneToOneField(PortalUser, on_delete=models.CASCADE)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
    position = models.ForeignKey(StaffPosition, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    def clean(self):
        if self.position.name == 'owner':
            if StaffPosition.objects.filter(
                    name__iexact='owner',
            ).exists():
                raise DjangoValidationError(
                    {'name': _('Cannot Assign two owners.')}
                )
