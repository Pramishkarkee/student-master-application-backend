from apps.core.models import BaseModel
from apps.students.models import CompleteProfileTracker
from apps.studentIdentity.models import Citizenship, Passport
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

        try:
            complete_profile_indicator=CompleteProfileTracker.objects.get(student=self._student_id)
            complete_profile_indicator.complete_citizenship_detail=True
            complete_profile_indicator.save()

        except CompleteProfileTracker.DoesNotExist:
            CompleteProfileTracker.objects.create(
                student=self._student_id,
                complete_citizenship_detail=True
            )


class AddPassportUseCase(BaseUseCase):
    def __init__(self , serializer ,student_id:str):
        self.serializer = serializer
        self._student_id =student_id
        self.data = serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        self._passport= Passport.objects.create(
            **self.data,
            student=self._student_id
        )
        try:
            complete_profile_indicator=CompleteProfileTracker.objects.get(student=self._student_id)
            complete_profile_indicator.complete_passport_field=True
            complete_profile_indicator.save()

        except CompleteProfileTracker.DoesNotExist:
            CompleteProfileTracker.objects.create(
                student=self._student_id,
                complete_passport_field=True
            )