from django.urls import path, include

# This file will contain all the end-points
urlpatterns = [
    path(
        '',
        include('apps.college.urls')
    ),
    path(
        'student/',
        include('apps.student.urls')
    ),
    path(
        'consultancy/',
        include('apps.consultancy.urls')
    ),
    path(
        'auth/',
        include('apps.auth.urls')
    )
]
