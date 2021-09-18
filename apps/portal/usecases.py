from apps.core.usecases import BaseUseCase
from apps.portal.models import Portal, PortalStaff, PortalStaffPosition
from apps.user.models import PortalUser


class RegisterConsultancyUseCase(BaseUseCase):
    def __init__(self,serializer):
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
            portal_staff_position = PortalStaffPosition.objects.create(name='owner')

            # 3. consultancy staff
            staff = PortalStaff.objects.create(
                user=user,
                portal=portal,
                position = portal_staff_position
            )