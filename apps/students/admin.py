from django.contrib import admin

# Register your models here.
from apps.students import models
from apps.core.admin import BaseModelAdmin


@admin.register(models.StudentModel)
class StudentAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )



