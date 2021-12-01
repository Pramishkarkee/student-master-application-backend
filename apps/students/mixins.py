from apps.students.usecases import GetStudentUseCase,GetAddressUseCase


class StudentMixin:
    def get_student(self):
        return GetStudentUseCase(student_id=self.kwargs.get('student_id')).execute()

class AddressMixin:
    def get_address(self):
        return GetAddressUseCase(student_id=self.kwargs.get('student_id')).execute()