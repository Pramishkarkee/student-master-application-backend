from django.contrib import admin

# Register your models here.
from apps.core.admin import BaseModelAdmin
from apps.portal import models


@admin.register(models.Portal)
class PortalAdmin(BaseModelAdmin):
    pass