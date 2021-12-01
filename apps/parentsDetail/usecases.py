from apps.students.models import CompleteProfileTracker
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.core.usecases import BaseUseCase
from apps.parentsDetail.models import StudentParents

class AddParentsUseCase(usecases.CreateUseCase):
    def __init__(self, serializer ,student):
        self._student = student
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        StudentParents.objects.create(
            student=self._student,
            **self._data
        )
        try:
            complete_profile_indicator=CompleteProfileTracker.objects.get(student=self._student)
            complete_profile_indicator.complete_parents_detail=True
            complete_profile_indicator.save()

        except CompleteProfileTracker.DoesNotExist:
            CompleteProfileTracker.objects.create(
                student=self._student,
                complete_parents_detail=True
            )

