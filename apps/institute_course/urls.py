from django.urls import path

from apps.institute_course import views

urlpatterns = [
    path(
        '<str:institute_id>/add',
        views.AddInstituteCourse.as_view(),
        name = 'add-gallery'
    ),
    path(
        '<institute_id>/get',
        views.ListInstituteCourse.as_view(),
        name = 'get-institute-course'
    ),
    path(
        '<institute_course_id>/update',
        views.UpdateInstituteCourse.as_view(),
        name = 'update-course'
    ),
    path(
        '<institute_course_id>/delete',
        views.DeleteInstituteCourseView.as_view(),
        name = 'delete-course'
    ),
    path(
        'listfaculty',
        views.ListFacultyView.as_view(),
        name = 'list-faculty'
    ),
    path(
        '<faculty_id>/listcourse',
        views.ListCourseView.as_view(),
        name='list course'
    ),
    path(
        'apply',
        views.ApplyInstituteCourseView.as_view(),
        name = 'apply'
    ),
]
