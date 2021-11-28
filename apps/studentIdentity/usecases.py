from apps.studentIdentity.models import Citizenship
from django.utils.datetime_safe import datetime
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.core.usecases import BaseUseCase


class AddCitizenshipUseCase(BaseUseCase):
    def __init__(self , serializer ,student_id:str):
        self.serializer = serializer
        self._student_id =student_id
        self.data = serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        self._citizenship = Citizenship(
            **self.data,
            student = self._student_id
        )
        self._citizenship.save()
