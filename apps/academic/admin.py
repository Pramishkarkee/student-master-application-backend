from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.academic import models


@admin.register(models.Academic)
class AcademicAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'student',
    )
