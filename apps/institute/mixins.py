from apps.institute import usecase

class InstituteMixins:
    def get_institute(self):
        return usecase.GetInstituteUseCase(
            institute_id=self.kwargs.get('institute_id')
        ).execute()

class ScholorshipMixins:
    def get_scholorship(self):
        return usecase.GetScholorshipUseCase(
            scholorship_id = self.kwargs.get('scholorship_id')
        ).execute()