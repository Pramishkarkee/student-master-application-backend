from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core import fields
from apps.portal.models import Portal

User = get_user_model()


class PortalSerializer(serializers.Serializer):
    class Meta:
        model = Portal
        fields = '__all__'


class RegisterPortalSerializer(PortalSerializer):
    email = serializers.EmailField(write_only=True)
    password = fields.PasswordField()

    class Meta(PortalSerializer.Meta):
        fields = (
            'name',
            'email',
            'password',
            'address',
            'contact',
            'profile_picture',
        )

    default_error_messages = {
        'duplicate_email': _('Email already exists try another one.')
    }

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                self.fail('duplicate_email')
            )
        return email
