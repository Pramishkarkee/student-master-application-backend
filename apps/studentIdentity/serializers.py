from django.db import models
from django.db.models import fields
from rest_framework import serializers

from apps.studentIdentity.models import Citizenship, Passport

class StudentCitizenshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizenship
        fields = (
            'citizenship_number',
            'issue_date',
            'issue_from',
            'front_page',
            'back_page'
        )


class StudentPassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = (
            'passport_number',
            'issue_date',
            'expire_date',
            'issue_from',
            'passport_image'
        )