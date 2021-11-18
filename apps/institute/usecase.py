from apps import institute
from apps.staff.models import StaffPosition
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


from apps.core import usecases
from apps.core.usecases import BaseUseCase
from apps.notification.mixins import NotificationMixin
from apps.institute.models import Institute, InstituteStaff,InstituteUser
from apps.settings.models import Settings

class RegisterInstituteUsecase(usecases.CreateUseCase, NotificationMixin):
    notification_group = ['portel_user']

    def execute(self):
        super(RegisterInstituteUsecase, self).execute()
        self.send_notification()

    def _factory(self):
        # create consultancy user
        user = InstituteUser.objects.create(
            email=self._data.pop("email"),
            password=(self._data.pop("password"))
        )

        #2. Institute
        self._institute =  Institute.objects.create(
            **self._data
        )
        role,created = StaffPosition.objects.get_or_create(name='owner')

        Settings.objects.create(user=user)

        #3. institute staff
        InstituteStaff.objects.create(
            user=user,
            institute=self._institute,
            role=role
        )
    def get_notification_data(self):
        return {
            'name': 'Institute Registered',
            'image': self._institute.logo.url,
            'content': 'Institute: {} Registered.'.format(self._institute.name),
            'id': str(self._institute.id)
        }