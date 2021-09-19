from apps.user.usecases import consultancy_user_usecases, portal_user_usecases


class ConsultancyUserMixin:
    def get_consultancy_user(self):
        return consultancy_user_usecases.GetConsultancyUserUseCase(
            user_id=self.kwargs.get('user_id')
        ).execute()


class PortalUserMixin:
    def get_portal_user(self):
        return portal_user_usecases.GetPortalUserUseCase(
            user_id=self.kwargs.get('user_id')
        ).execute()
