from apps.institute_course.usecases import GetInstituteClassUseCase

class InstituteCourseMixin:
    def get_institute(self):
        return GetInstituteClassUseCase(
            institute_id=self.kwargs.get('institute_id')
        ).execute()

