from django.db import models

# Create your models here.
from apps.core.models import BaseModel


class StaffPosition(BaseModel):
    name = models.CharField(max_length=20)

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(StaffPosition, self).save(*args, **kwargs)
