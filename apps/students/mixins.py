from apps.students.usecases import GetStudentUseCase


class StudentMixin:
    def get_student(self):
        print("**********************************mixins")
        return GetStudentUseCase(student_id=self.kwargs.get('student_id')).execute()
