from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.notification.mixins import NotificationMixin
from apps.students.models import StudentUser, StudentModel
from apps.core import usecases
from apps.settings.models import Settings
from apps.core.usecases import BaseUseCase
from apps.students.exceptions import StudentModelNotFound


class RegisterStudentUseCase(usecases.CreateUseCase, NotificationMixin):
    notification_group = ['portal_user']

    def execute(self):
        super(RegisterStudentUseCase, self).execute()
        self.send_notification()

    def _factory(self):
        # 1. create consultancy user
        # print(self._data.pop("email"))
        user = StudentUser.objects.create(
            email=self._data.pop('email'),
            password=self._data.pop('password')
        )
        # 2. consultancy
        self._student = StudentModel.objects.create(
            user=user,
            **self._data
        )

        Settings.objects.create(user=user)

    def get_notification_data(self):
        return {
            'name': 'Consultancy Registered',
            'image': self._student.image.url,
            'content': 'Consultancy: {} Registered.'.format(self._student.name),
            'id': str(self._student.id)
        }


class GetStudentUseCase(BaseUseCase):
    def __init__(self,student_id:str):
        self._student_id =student_id

    def execute(self):
        self._factory()
        print("mixins**************")
        return self._student

    def _factory(self):
        try:
            self._student = StudentModel.objects.get(pk=self._student_id)

        except StudentModel.DoesNotExist:
            raise StudentModelNotFound

class GetStudentUserUseCase(BaseUseCase):
    def __init__(self,student):
        self._student_id =student

    def execute(self):
        self._factory()
        return self._student

    def _factory(self):
        try:
            student = StudentModel.objects.filter(id=self._student_id)

            self._student = {'student': student}
        except StudentModel.DoesNotExist:
            raise StudentModelNotFound
