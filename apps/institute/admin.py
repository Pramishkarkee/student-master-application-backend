from django.contrib import admin

from apps.institute import models
from apps.core.admin import BaseModelAdmin


# Register your models here.
@admin.register(models.Institute)
class InstituteAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )


@admin.register(models.InstituteStaff)
class InstituteStaffAdmin(BaseModelAdmin):
    list_filter = BaseModelAdmin.list_filter+(
        'institute',
    )   
