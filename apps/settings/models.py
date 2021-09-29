from django.db import models

# Create your models here.
from apps.core.models import BaseModel


class Settings(BaseModel):
    color = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        default='#800000'
    )

