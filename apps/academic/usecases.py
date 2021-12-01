from apps import students
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.core.usecases import BaseUseCase
from apps.academic.models import Academic, PersonalEssay, StudentLor, StudentSop
from apps.students.models import CompleteProfileTracker

class CreateStudentAcademicUseCase(usecases.CreateUseCase):
    def __init__(self, serializer,student):
        self._student = student
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        #1. create Academic
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
            

class CreateStudentSopUseCase(usecases.CreateUseCase):
    def __init__(self, serializer ,student):
        self._student = student
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        #1. create Academic
        self._academic=StudentSop.objects.create(
            student=self._student,
            **self._data
        )
        try:
            complete_profile=CompleteProfileTracker.objects.get(student=self._student)
            complete_profile.complete_sop_field=True
            complete_profile.save()
        except CompleteProfileTracker.DoesNotExist:
            CompleteProfileTracker.objects.create(
                student=self._student,
                complete_sop_field=True) 

class CreateStudentLorUseCase(usecases.CreateUseCase):
    def __init__(self, serializer ,student):
        self._student = student
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        #1. create student lor
        self._academic=StudentLor.objects.create(
            student=self._student,
            **self._data
        )
        try:
            complete_profile=CompleteProfileTracker.objects.get(student=self._student)
            complete_profile.complete_lor_field=True
            complete_profile.save()
        except CompleteProfileTracker.DoesNotExist:
            CompleteProfileTracker.objects.create(
                student=self._student,
                complete_lor_field=True) 



class CreateStudentEssayUseCase(usecases.CreateUseCase):
    def __init__(self, serializer ,student):
        self._student = student
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        #1. create personal essay
        self._academic=PersonalEssay.objects.create(
            student=self._student,
            **self._data
        )
        try:
            complete_profile=CompleteProfileTracker.objects.get(student=self._student)
            complete_profile.complete_personalessay_field=True
            complete_profile.save()
        except CompleteProfileTracker.DoesNotExist:
            CompleteProfileTracker.objects.create(
                student=self._student,
                complete_personalessay_field=True) 
