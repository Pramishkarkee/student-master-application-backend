from django.urls import path

from apps.students import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path(
        'register',
        views.RegisterStudentView.as_view(),
        name='register-institute'
    ),
    path(
        '<student_id>/student-profile',
        views.StudentInitProfileView.as_view(),
        name='student-init-view'
    ),

    path(
        '<student_id>/student-address',
        views.StudentAddressView.as_view(),
        name = 'student address view'
    )

]
urlpatterns = format_suffix_patterns (urlpatterns)

