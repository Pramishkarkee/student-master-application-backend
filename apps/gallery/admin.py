from django.contrib import admin

# Register your models here.
from apps.core.admin import BaseModelAdmin
from apps.gallery.models import Gallery


@admin.register(Gallery)
class RelationAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display+(
        'title',
    )
