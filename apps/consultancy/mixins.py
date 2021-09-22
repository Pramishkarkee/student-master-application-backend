from apps.consultancy.usecases import GetConsultancyUseCase


class ConsultancyMixin:
    def get_consultancy(self):
        return GetConsultancyUseCase(consultancy_id=self.kwargs.get('consultancy_id')).execute()
