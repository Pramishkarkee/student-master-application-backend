from django.contrib import admin

from apps.consultancy import models
from apps.core.admin import BaseModelAdmin


@admin.register(models.Consultancy)
class ConsultancyAdmin(BaseModelAdmin):
    pass


@admin.register(models.ConsultancyStaff)
class ConsultancyStaffAdmin(BaseModelAdmin):
    pass


@admin.register(models.ConsultancyStaffPosition)
class ConsultancyStaffPositionAdmin(BaseModelAdmin):
    pass
