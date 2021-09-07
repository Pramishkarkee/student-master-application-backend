from apps.consultancy.models import Consultancy, ConsultancyStaff
from apps.core import usecases
from apps.user.models import ConsultancyUser


class RegisterConsultancyUseCase(usecases.CreateUseCase):
    def _factory(self):
        # 1. create consultancy user
        user = ConsultancyUser.objects.create(
            email=self._data.pop('email'),
            password=self._data.pop('password')
        )
        # 2. consultancy
        consultancy = Consultancy.objects.create(
            **self._data
        )

        # 3. consultancy staff
        staff = ConsultancyStaff.objects.create(
            user=user,
            consultancy=consultancy
        )
