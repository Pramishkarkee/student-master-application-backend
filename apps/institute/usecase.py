from datetime import datetime
from apps.institute.exceptions import InstituteNotFound, InstituteScholorshipDoesntExist
from apps import institute
from apps.staff.models import StaffPosition
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


from apps.core import usecases
from apps.core.usecases import BaseUseCase, CreateUseCase
from apps.notification.mixins import NotificationMixin
from apps.institute.models import Institute, InstituteScholorship, InstituteStaff,InstituteUser
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


class ListInstituteUseCase(BaseUseCase):
    def execute(self):
        self._factory()
        return self._institute

    def _factory(self):
        self._institute = Institute.objects.all()


class GetInstituteUseCase(BaseUseCase):
    def __init__(self,institute_id:str):
        self._institute_id = institute_id

    def execute(self):
        self._factory()
        return self._institute

    def _factory(self):
        try:
            self._institute = Institute.objects.get(pk=self._institute_id)

        except Institute.DoesNotExist:
            raise InstituteNotFound



class AddScholorshipUseCase(usecases.CreateUseCase):
    def __init__(self,serializer,institute):
        self._institute = institute
        self._data=serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        InstituteScholorship.objects.create(
            institute = self._institute,
            **self._data
        )
class GetScholorshipUseCase(BaseUseCase):
    def __init__(self,scholorship_id):
        self._scholorship_id = scholorship_id

    def execute(self):
        self._factory()
        return self._scholorship 
    
    def _factory(self):
        try:
            self._scholorship = InstituteScholorship.objects.get(pk=self._scholorship_id)

        except InstituteScholorship.DoesNotExist:
            raise InstituteScholorshipDoesntExist

class UpdateScholorshipUseCase(BaseUseCase):
    def __init__(self,serializer,scholorship: InstituteScholorship):
        self.serializer = serializer
        self._data = serializer.validated_data
        self._schlorship=scholorship

    def execute(self):
        self._factory()

    def _factory(self):
        for key in self._data.keys():
            setattr(self._schlorship,key,self._data.get(key))

        self._schlorship.updated_at =datetime.now()
        self._schlorship.save()


class ListScholorshipUseCase(BaseUseCase):
    def __init__(self,institute):
        self._institute = institute

    def execute(self):
        self._factory()
        return self._scholorship

    def _factory(self):
        self._scholorship = InstituteScholorship.objects.filter(institute = self._institute)


class DeleteScholorshipUseCase(BaseUseCase):
    def __init__(self,scholorship):
        self._scholorship = scholorship

    def execute(self):
        return self._factory()

    def _factory(self):
        self._scholorship.delete()