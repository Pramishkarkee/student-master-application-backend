import re

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.students.models import StudentModel
from apps.core import fields
User = get_user_model()


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'


class RegisterStudentSerializer(StudentSerializer):
    email = serializers.EmailField(write_only=True)
    password = fields.PasswordField()

    class Meta(StudentSerializer.Meta):
        fields = (
            'name',
            'email',
            'password',
            'contact',
            'latitude',
            'longitude',
            'image'
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
        if not matched:
            raise serializers.ValidationError(
                self.fail('password_requirement_failed')
            )
        return value


class StudentDetailSerializer(StudentSerializer):
    # user = serializers.CharField()

    class Meta(StudentSerializer.Meta):
        fields = (
            'name',
            'contact',
            'latitude',
            'longitude',
            'image'
        )
