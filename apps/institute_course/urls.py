from django.urls import path

from apps.institute_course import views

urlpatterns = [
    path(
        '<str:institute_id>/add',
        views.AddInstituteCourse.as_view(),
        name = 'add-gallery'
    ),
]
