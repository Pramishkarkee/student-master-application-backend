from apps.core.usecases import BaseUseCase
from apps.portal.models import Portal, PortalStaff
from apps.staff.models import StaffPosition
from apps.user.models import PortalUser


class RegisterPortalUseCase(BaseUseCase):
    def __init__(self, serializer):
        self._serializer = serializer
        self._data = serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        def _factory(self):
            # 1. create portal user
            user = PortalUser.objects.create(
                email=self._data.pop('email'),
                password=self._data.pop('password')
            )
            # 2. consultancy
            portal = Portal.objects.create(
                **self._data
            )
            staff_position = StaffPosition.objects.get_or_create(name='owner')

            # 3. consultancy staff
            staff = PortalStaff.objects.create(
                user=user,
                portal=portal,
                position=staff_position
            )
