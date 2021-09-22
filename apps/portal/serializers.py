from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core import fields
from apps.portal.models import Portal, PortalStaff

User = get_user_model()


class PortalSerializer(serializers.ModelSerializer):
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
            'country',
            'city',
            'state',
            'profile_picture',
            'street_address',
            'latitude',
            'longitude',
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


class PortalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalStaff
        fields = '__all__'


class CreatePortalStaffSerializer(PortalStaffSerializer):
    email = serializers.EmailField()
    password = fields.PasswordField()
    fullname = serializers.CharField()

    class Meta(PortalStaffSerializer.Meta):
        fields = (
            'email',
            'password',
            'position',
            'fullname',
        )

    default_error_messages = {
        'duplicate_email': _('Email already exists try another one.'),
        'short_password_length': _('Password must be of minimum 8 length.')
    }

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                self.fail('duplicate_email')
            )
        return value

    def validate_password(self, value):
        password = len(value)
        if password < 8:
            raise serializers.ValidationError(
                self.fail('short_password_length')
            )
        return value
