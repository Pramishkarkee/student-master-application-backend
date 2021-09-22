from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.consultancy.models import Consultancy, ConsultancyStaff
from apps.core import fields

User = get_user_model()


class ConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultancy
        fields = '__all__'


class RegisterConsultancySerializer(ConsultancySerializer):
    email = serializers.EmailField(write_only=True)
    password = fields.PasswordField()

    class Meta(ConsultancySerializer.Meta):
        fields = (
            'name',
            'email',
            'password',
            'contact',
            'country',
            'city',
            'state',
            'street_address',
            'latitude',
            'longitude',
            'website',
            'logo',
            'cover_image',
            'about',
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


class ConsultancyStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultancyStaff
        fields = '__all__'


class CreateConsultancyStaffSerializer(ConsultancyStaffSerializer):
    email = serializers.EmailField()
    password = fields.PasswordField()
    fullname = serializers.CharField()

    class Meta(ConsultancyStaffSerializer.Meta):
        fields = (
            'email',
            'password',
            'fullname',
            'position'
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
