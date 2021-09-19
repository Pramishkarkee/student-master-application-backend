from django.utils.translation import  gettext_lazy as _
from rest_framework.exceptions import NotFound

from apps.core.usecases import BaseUseCase
from apps.user.models import PortalUser


class PortalUserNotFound(NotFound):
    default_detail = _('User Not Found for following Id.')


class GetPortalUserUseCase(BaseUseCase):
    def __init__(self, user_id):
        self._user_id = user_id

    def execute(self):
        self._factory()
        return self._user

    def _factory(self):
        try:
            self._user = PortalUser.objects.get(pk=self._user_id)
        except PortalUser.DoesNotExist:
            raise PortalUserNotFound