import re

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.core import fields

from apps.academic.models import Academic

class CreateAcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic
        fields = (
            'institute_name',
            'duration',
            'level',
            'score',
            'full_score',
            'marksheet',
            'certificate'
        )