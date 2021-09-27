from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.consultancy import tasks
from apps.consultancy.emails import SendEmailToConsultanySTaff
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


class GetConsultancyStaffUseCase(BaseUseCase):
    def __init__(self, consultancy_staff_id: ConsultancyStaff):
        self._consultancy_staff_id = consultancy_staff_id

    def execute(self):
        self._factory()
        return self.consultancy_staff

    def _factory(self):
        try:
            self.consultancy_staff = ConsultancyStaff.objects.get(pk=self._consultancy_staff_id)
        except ConsultancyStaff.DoesNotExist:
            raise ConsultancyNotFound


class CreateConsultancyStaffUseCase(usecases.CreateUseCase):
    def __init__(self, serializer, consultancy: Consultancy):
        self._consultancy = consultancy
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        user = {
            'email': self._data.pop('email'),
            'fullname': self._data.pop('fullname'),
        }
        # 1. create consultancy user
        self.consultancy_user = ConsultancyUser.objects.create(
            **user
        )
        # 2. consultancy staff
        try:
            consultancy_staff = ConsultancyStaff.objects.create(
                user=self.consultancy_user,
                consultancy=self._consultancy,
                role=self._data['role'],
                profile_photo=self._data['profile_photo']
            )
            consultancy_staff.clean()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)
        context = {
            'uuid': self.consultancy_user.id,
            'name': self._consultancy.name,
            'user_email':self.consultancy_user.email,
        }
        tasks.send_set_password_email_to_user.apply_async(
            kwargs=context
        )

        # without celery
        # SendEmailToConsultanySTaff(
        #     context={
        #         'uuid': self.consultancy_user.id,
        #         'name': self._consultancy.name
        #     }
        # ).send(to=[self.consultancy_user.email])


class CreatePasswordForConsultancyUserUseCase(usecases.CreateUseCase):
    def __init__(self, serializer, consultancy_user: ConsultancyUser):
        self._consultancy_user = consultancy_user
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        password = self._data.pop('password')
        self._consultancy_user.set_password(password)
        self._consultancy_user.save()


class UpdateConsultancyStaffUseCase(BaseUseCase):
    def __init__(self, serializer, consultancy_staff: ConsultancyStaff):
        self._consultancy_staff = consultancy_staff
        self._serializer = serializer
        self._data = self._serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        email = self._data.pop('email')
        fullname = self._data.pop('fullname')
        for data in self._data.keys():
            setattr(self._consultancy_staff, data, self._data[data])
        try:
            self._consultancy_staff.clean()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)
        self._consultancy_staff.updated_at = timezone.now()
        self._consultancy_staff.save()
        user = self._consultancy_staff.user
        user.email = email
        user.fullname = fullname
        user.updated_at = timezone.now()
        user.save()


class ListConsultancyStaffUseCase(BaseUseCase):
    def __init__(self, consultancy: Consultancy):
        self._consultancy = consultancy

    def execute(self):
        self._factory()
        return self._consultancy_staff

    def _factory(self):
        self._consultancy_staff = ConsultancyStaff.objects.filter(consultancy=self._consultancy)


class ListConsultancyUseCase(BaseUseCase):
    def execute(self):
        self._factory()
        return self._consultancy

    def _factory(self):
        self._consultancy = Consultancy.objects.all()
