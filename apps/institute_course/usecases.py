
from apps import institute
from django.utils.datetime_safe import datetime
from rest_framework.exceptions import ValidationError
from  django.utils.translation import  gettext_lazy as _

from apps.core.usecases import BaseUseCase
from apps.institute_course.models import InstituteCourse,Course,Faculty
from apps.institute.models import Institute
from apps.institute_course.exceptions import CourseNotFound, FacultyNotFound, InstituteNotFound



        

class AddCourseUseCase(BaseUseCase):

    def __init__(self , serializer ,institute:str):
        self._institute= institute
        self._serializer=serializer



    def execute(self):
        self._factory()

    def _factory(self):

        print("this is *inst",self._institute)
        try:
            course=Course.objects.get(pk=self._serializer.data.pop('course'))
        except Course.DoesNotExist:
            raise CourseNotFound

        try:
            faculty=Faculty.objects.get(pk=self._serializer.data.pop('faculty'))

        except Faculty.DoesNotExist:
            raise FacultyNotFound
        
        # del self._serializer.data['faculty']
        # print("*************delete",self._serializer.data['faculty'])
        self._course = InstituteCourse.objects.create(
            program=self._serializer.data.pop('program'),
            faculty = faculty,
            course = course,
            intake = self._serializer.data.pop('intake'),
            eligibility = self._serializer.data.pop('eligibility'),
            score = self._serializer.data.pop('score'),
            last_mini_academic_score = self._serializer.data.pop('last_mini_academic_score'),
            duration_year = self._serializer.data.pop('duration_year'),
            total_fee = self._serializer.data.pop('total_fee'),
            fee_currency = self._serializer.data.pop('fee_currency'),
            reg_status = self._serializer.data.pop('reg_status'),
            reg_open = self._serializer.data.pop('reg_open'),
            reg_close = self._serializer.data.pop('reg_close'),
            institute=self._institute
            )
        # self._course.save()

    

class GetInstituteCourseUseCase(BaseUseCase):
    def __init__(self,inst):
        self._institute = inst

    def execute(self):
        self._factory()
        return self._course

    def _factory(self):
        self._course = InstituteCourse.objects.filter(institute=self._institute).prefetch_related('course','faculty')
    


class GetCourseUseCase(BaseUseCase):
    def __init__(self,institute_course_id):
        self._course_id = institute_course_id

    def execute(self):
        self._factory()
        return self._course

    def _factory(self):
        try:
            self._course = InstituteCourse.objects.get(pk=self._course_id)
        except InstituteCourse.DoesNotExist:
            raise CourseNotFound


class UpdateInstituteCourseUseCase(BaseUseCase):
    def __init__(self,serializer,institute_course:InstituteCourse):
        self._institute_course =institute_course
        self._serializer = serializer
        self._data = serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        for key in self._data.keys():
            setattr(self._institute_course,key,self._data.get(key))

        self._institute_course.updated_at = datetime.now()
        self._institute_course.save()


class DeleteInstituteCourseUseCase(BaseUseCase):
    def __init__(self,institute_course):
        self._institute_course = institute_course

    def execute(self):
        self._institute_course.delete()

class ListFacultyUseCase(BaseUseCase):
    def execute(self):
        return Faculty.objects.all()


class GetFacultyUseCase(BaseUseCase):
    def __init__(self,faculty_id):
        self._faculty = faculty_id

    def execute(self):
        return self._faculty

    def _factory(self):
        try:
            self._faculty = Faculty.objects.filter(pk = self._factory)

        except Faculty.DoesNotExist:
            raise FacultyNotFound


class ListCourseUseCase(BaseUseCase):
    def __init__(self,faculty):
        self._faculty = faculty

    def execute(self):
        self._course = Course.objects.filter(faculty = self._faculty)
        return self._course