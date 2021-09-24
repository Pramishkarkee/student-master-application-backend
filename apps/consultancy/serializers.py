import re

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
        'duplicate_email': _('Email already exists try another one.'),
        'password_requirement_failed': _(
            'Password must 8 character  with one digit,one lowercase,one uppercase and special character.')
    }

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                self.fail('duplicate_email')
            )
        return value

    def validate_password(self, value):
        """
        Rule 1. Password must be 8 length at minimum
        Rule 2. Password must contain one digit,one lowercase,one uppercase and special character.
        """
        pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        matched = re.match(pattern, value)
        print(matched)
        if not matched:
            raise serializers.ValidationError(
                self.fail('password_requirement_failed')
            )
        return value


class ConsultancyStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultancyStaff
        fields = '__all__'


class CreateConsultancyStaffSerializer(ConsultancyStaffSerializer):
    email = serializers.EmailField()
    fullname = serializers.CharField()

    class Meta(ConsultancyStaffSerializer.Meta):
        fields = (
            'email',
            'fullname',
            'role',
            'profile_photo',
        )

    default_error_messages = {
        'duplicate_email': _('Email already exists try another one.'),
        # 'password_requirement_failed': _(
        #     'Password must 8 character  with one digit,one lowercase,one uppercase and special character.')
    }

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                self.fail('duplicate_email')
            )
        return value


class ListConsultancyStaffSerializer(ConsultancyStaffSerializer):
    consultancy = serializers.CharField()
    email = serializers.CharField(source='get_consultancy_user_email')
    fullname = serializers.CharField(source='get_consultancy_full_name')

    class Meta(ConsultancyStaffSerializer.Meta):
        fields = (
            'id',
            'consultancy',
            'email',
            'fullname',
            'role',
            'profile_photo',
        )


class UpdateConsultancyStaffSerializer(CreateConsultancyStaffSerializer):
    pass


class CreatePasswordForConsultancyStaffSerializer(serializers.Serializer):
    password = fields.PasswordField()

    default_error_messages = {
        'password_requirement_failed': _(
            'Password must 8 character  with one digit,one lowercase,one uppercase and special character.')
    }

    def validate_password(self, value):
        """
        Rule 1. Password must be 8 length at minimum
        Rule 2. Password must contain one digit,one lowercase,one uppercase and special character.
        """
        pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        matched = re.match(pattern, value)
        if not matched:
            raise serializers.ValidationError(
                self.fail('password_requirement_failed')
            )
        return value
