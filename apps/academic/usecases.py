from apps import students
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.core.usecases import BaseUseCase
from apps.academic.models import Academic
from apps.students.models import CompleteProfileTracker

class CreateStudentAcademicUseCase(usecases.CreateUseCase):
    def __init__(self, serializer,student):
        self._student = student
        super().__init__(serializer)

    def execute(self):
        print("**************************************")
        self._factory()

    def _factory(self):
        #1. create Academic
        print("**************************************",self._student)
        self._academic=Academic.objects.create(
            student=self._student,
            **self._data
        )
        try:
            complete_profile=CompleteProfileTracker.objects.get(student=self._student)
            complete_profile.complete_academic_detail=True
            complete_profile.save()
        except CompleteProfileTracker.DoesNotExist:
            CompleteProfileTracker.objects.create(
                student=self._student,
                complete_academic_detail=True) 
            