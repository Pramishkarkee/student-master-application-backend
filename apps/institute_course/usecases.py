
from apps.academic.models import PersonalEssay, StudentLor, StudentSop
from apps.auth.jwt import serializers
from apps.consultancy.exceptions import ConsultancyNotFound
from apps.consultancy.models import Consultancy
from apps.studentIdentity.models import Citizenship, Passport
from apps.students.exceptions import StudentModelNotFound
from apps.students.models import StudentModel
from apps import institute
from django.utils.datetime_safe import datetime
from rest_framework.exceptions import ValidationError
from  django.utils.translation import  gettext_lazy as _
from django.db.models import Count

from apps.core.usecases import BaseUseCase
from apps.institute_course.models import CommentApplicationInstitute, InstituteApply, InstituteCourse,Course,Faculty
from apps.institute.models import Institute, InstituteStaff
from apps.institute_course.exceptions import CourseNotFound, FacultyNotFound, InstituteApplyNotFound, InstituteNotFound, InstituteStaffNotFound


class AddCourseUseCase(BaseUseCase):

    def __init__(self , serializer ,institute:str):
        self._institute= institute
        self._serializer=serializer

    def execute(self):
        self._factory()

    def _factory(self):
        try:
            course=Course.objects.get(pk=self._serializer.data.pop('course'))
        except Course.DoesNotExist:
            raise CourseNotFound

        try:
            faculty=Faculty.objects.get(pk=self._serializer.data.pop('faculty'))

        except Faculty.DoesNotExist:
            raise FacultyNotFound
        
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


class ApplyUseCase(BaseUseCase):
    def __init__(self,serializer):
        self._serializer = serializer

    def execute(self):
        self._factory()

    def _factory(self):
        self.student=self._serializer.data['student'],
        self.course = self._serializer.data.pop('course'),
        self.consultancy= self._serializer.data.pop('consultancy'),
        self.institute = self._serializer.data.pop('institute'),
        self._get_instance()
        if self.consultancy[0]:
            data = {
                'student':self.student_instant,
                'course' :self.course_instant,
                'institute' : self.institute_instance,
                'consultancy' : self.consultancy_instance
            }
        else:
            data = {
                'student':self.student_instant,
                'course' :self.course_instant,
                'institute' : self.institute_instance
            }
        InstituteApply.objects.create(
            **data
        )

    def _get_instance(self):
        try:
            self.student_instant = StudentModel.objects.get(pk=str(self.student[0]))
        except StudentModel.DoesNotExist:
            raise StudentModelNotFound

        try:
            self.course_instant = InstituteCourse.objects.get(pk=str(self.course[0]))
        except InstituteCourse.DoesNotExist:
            raise CourseNotFound

        try:
            self.institute_instance = Institute.objects.get(pk = str(self.institute[0]))

        except Institute.DoesNotExist:
            raise InstituteNotFound

        try:
            if self.consultancy[0]:
                self.consultancy_instance = Consultancy.objects.get(pk = str(self.consultancy[0]))
            else:
                self.consultancy_instance = ""

        except Consultancy.DoesNotExist:
            raise InstituteNotFound

class ListStudentApplicationCourseUseCase(BaseUseCase):
    def __init__(self,institute):
        self._institute = institute

    def execute(self):
        self._factory()
        return self._apply

    def _factory(self):
        self._apply = InstituteApply.objects.filter(institute=self._institute)

            

class GetApplyInstitute(BaseUseCase):
    def __init__(self,apply_id):
        self.apply_id =apply_id

    def execute(self):
        self._factory()
        return self._apply

    def _factory(self):
        try:
            self._apply = InstituteApply.objects.get(pk = self.apply_id)

        except InstituteApply.DoesNotExist:
            raise InstituteApplyNotFound

class CancleStudentApplicationUseCase(BaseUseCase):
    def __init__(self,application,serializer):
        self._application = application
        self._data = serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        for key in self._data.keys():
            setattr(self._application,key,self._data.get(key))

        self._application.updated_at = datetime.now()
        self._application.save()

class AddCommentApplyInstitute(BaseUseCase):
    def __init__(self,serializer,apply):
        self._apply = apply
        self._serializer = serializer

    def execute(self):
        self._factory()

    def _factory(self):
        try:
            institutestaff=InstituteStaff.objects.get(pk = str(self._serializer.data.pop('institute_user')[0]))
        
        except InstituteStaff.DoesNotExist:
            raise InstituteStaffNotFound

        CommentApplicationInstitute.objects.create(
            application = self._apply,
            institute_user = institutestaff,
            comment = self._serializer.data.pop('comment')
        )

class ListCommentInstituteUseCase(BaseUseCase):
    def __init__(self,apply):
        self._apply = apply

    def execute(self):
        self._factory()
        return self._comment

    def _factory(self):
        self._comment=CommentApplicationInstitute.objects.filter(
            application = self._apply
        )


class ApplicationDashboardUsecase(BaseUseCase):
    def __init__(self,institute):
        self._institute = institute

    def execute(self):
        self._factory()
        return self.applicant

    def _factory(self):
        self.applicant=InstituteApply.objects.filter(
            institute=self._institute,
            # created_at__range=["2021-12-01", "2022-01-31"]
            ).values('action').annotate(Count('action'))


class SendedDocumentByStudent():
    def __init__(self,data):
        self._data = data
    def execute(self):
        self._factory()
    def _factory(self):
        course = ""
        citizenship=""
        passport=""
        essay =[]
        sop=[]
        lor=[]

        if len(self._data["courseId"])>1:
            try:
                course = InstituteCourse.objects.get(id=self._data['courseId'])
            except InstituteCourse.DoesNotExist:
                raise CourseNotFound

        for k in self._data.keys():  
            if k== "citizenship":
                if len(self._data[k])>1:
                    try:
                        citizenship = Citizenship.objects.get(pk=self._data[k])
                    except Citizenship.DoesNotExist:
                        raise ValidationError({'error': _('Citizenship  does not exist for following id.')})

            elif k == "passport":
                if len(self._data[k])>1:
                    try:
                        passport = Passport.objects.get(pk=self._data[k])
                    except Passport.DoesNotExist:
                        raise ValidationError({'error': _('Passport does not exist for following id')})

            elif k == "essay":
                if len(self._data[k])>0:
                    for essay_id in self._data[k]:
                        print("essay id",essay_id)
                        try:
                            getessay = PersonalEssay.objects.get(pk=essay_id)
                            sopobj={
                                "essay":getessay,
                                "course":course
                            }
                            essay.append(sopobj)
                        except PersonalEssay.DoesNotExist:
                            raise ValidationError({'error': _('Essay does not exist for following id')})
            
            elif k == "sop":
                if len(self._data[k])>0:
                    for sop_id in self._data[k]:
                        try:
                            getSop = StudentSop.objects.get(pk=sop_id)
                            sopObj={
                                "sop":getSop,
                                "course":course
                            }
                            sop.append(sopObj)
                        except StudentSop.DoesNotExist:
                            raise ValidationError({'error': _('Passport does not exist for following id')})
            
            elif k == "lor":
                if len(self._data[k])>0:
                    for lor_id in self._data[k]:
                        try:
                            getLor = StudentLor.objects.get(pk=lor_id)
                            lorObj={
                                'lor':getLor,
                                'course':course
                            }
                            lor.append(lorObj)
                        except StudentLor.DoesNotExist:
                            raise ValidationError({'error': _('Passport does not exist for following id')})

        def _AddDataIntoTable(self, data):
            print("87364836")


        





