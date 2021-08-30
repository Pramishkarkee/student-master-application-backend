from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseModelAdmin
from apps.user import models

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'fullname', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': (
            'fullname',
            'contact_number',
        )}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'is_archived',
                'is_portal_user', 'groups', 'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'fullname',
                'password1',
                'password2',
                'is_portal_user'
            ),
        }),
    )
    ordering = ('-date_joined',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_archived', 'groups')
    search_fields = ('username', 'fullname', 'email')


@admin.register(models.NormalUser)
class NormalUserAdmin(BaseModelAdmin):
    list_display = (
        'id',
        'email',
        'is_active',
        'updated_at'
    )
    list_filter = BaseModelAdmin.list_filter + (
        'user__is_active',
    )

    def email(self, instance):
        return instance.user.email

    def is_active(self, instance):
        return instance.user.is_active
