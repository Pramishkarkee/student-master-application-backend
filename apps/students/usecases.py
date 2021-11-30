from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.notification.mixins import NotificationMixin
from apps.students.models import StudentAddress, StudentUser, StudentModel, CompleteProfileTracker
from apps.core import usecases
from apps.settings.models import Settings
from apps.core.usecases import BaseUseCase
from apps.students.exceptions import StudentAddressUnique, StudentModelNotFound


class RegisterStudentUseCase(usecases.CreateUseCase, NotificationMixin):
    notification_group = ['portal_user']

    def execute(self):
        super(RegisterStudentUseCase, self).execute()
        self.send_notification()

    def _factory(self):
        # 1. create consultancy user

        user = StudentUser.objects.create(
            email=self._data.pop('email'),
            password=self._data.pop('password'),
            fullname=self._data.pop('fullname')
        )
        # 2. consultancy
        self._student = StudentModel.objects.create(
            user=user,
            **self._data
        )

        Settings.objects.create(user=user)

    def get_notification_data(self):
        return {
            'name': 'Student Registered',
            'image': self._student.image.url,
            'content': 'Student: {} Registered.'.format(self._student.fullname),
            'id': str(self._student.id)
        }

class GetStudentUseCase(BaseUseCase):
    def __init__(self,student_id:str):
        self._student_id =student_id

    def execute(self):
        
        self._factory()
        return self._student

    def _factory(self):
        try:
            self._student = StudentModel.objects.get(pk=self._student_id)

        except StudentModel.DoesNotExist:
            raise StudentModelNotFound

class AddStudentAddressUseCase(usecases.CreateUseCase,GetStudentUseCase):
    def __init__(self, serializer,student_id:str):
        self._student_id= student_id
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        # add student address

        StudentAddress.objects.create(
                **self._data,
                student=self._student_id
            )

        # get complete profile indicator
        try:
            complete_profile_indicator=CompleteProfileTracker.objects.get(student=self._student_id).update(complete_address = True)

        except CompleteProfileTracker.DoesNotExist:
             CompleteProfileTracker.objects.create(
                 student=self._student_id,
                 complete_address = True
             )
        

        # complete profile update




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
