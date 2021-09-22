from rest_framework.exceptions import ValidationError

from apps.consultancy.exceptions import ConsultancyNotFound
from apps.consultancy.models import Consultancy, ConsultancyStaff
from apps.core import usecases
from apps.core.usecases import BaseUseCase
from apps.staff.models import StaffPosition
from apps.user.models import ConsultancyUser
from django.core.exceptions import ValidationError as DjangoValidationError


class RegisterConsultancyUseCase(usecases.CreateUseCase):
    def _factory(self):
        # 1. create consultancy user
        user = ConsultancyUser.objects.create(
            email=self._data.pop('email'),
            password=(self._data.pop('password'))
        )
        # 2. consultancy
        consultancy = Consultancy.objects.create(
            **self._data
        )
        position, created = StaffPosition.objects.get_or_create(name='owner')
        # 3. consultancy staff
        staff = ConsultancyStaff.objects.create(
            user=user,
            consultancy=consultancy,
            position=position
        )


class GetConsultancyUseCase(BaseUseCase):
    def __init__(self, consultancy_id: Consultancy):
        self._consultancy_id = consultancy_id

    def execute(self):
        self._factory()
        return self._consultancy

    def _factory(self):
        try:
            self._consultancy = Consultancy.objects.get(pk=self._consultancy_id)
        except Consultancy.DoesNotExist:
            raise ConsultancyNotFound


class CreateConsultancyStaffUseCase(usecases.CreateUseCase):
    def __init__(self, serializer, consultancy: Consultancy):
        self._consultancy = consultancy
        print(self._consultancy)
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        user = {
            'email': self._data.pop('email'),
            'password': (self._data.pop('password')),
            'fullname': self._data.pop('fullname'),
        }
        # 1. create consultancy user
        consultancy_user = ConsultancyUser.objects.create(
            **user

        )
        # 2. consultancy staff
        try:
            consultancy_staff = ConsultancyStaff.objects.create(
                user=consultancy_user,
                consultancy=self._consultancy,
                position=self._data['position']
            )
            consultancy_staff.clean()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)
