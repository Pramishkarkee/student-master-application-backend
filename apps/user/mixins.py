from apps.user.usecases import consultancy_user_usecases


class ConsultancyUserMixin:
    def get_consultancy_user(self):
        return consultancy_user_usecases.GetConsultancyUserUseCase(
            user_id=self.kwargs.get('user_id')
        ).execute()
