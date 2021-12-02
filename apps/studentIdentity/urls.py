from django.urls import path
from apps.studentIdentity import views

urlpatterns = [
    path(
        '<student_id>/citizenship/add',
        views.AddCitizenshipView.as_view(),
        name = 'add-citizenship'
    ),
    path(
        '<student_id>/passport/add',
        views.AddPassportView.as_view(),
        name = 'add-passport'
    ),
    path(
        'passport/<student_id>/get',
        views.GetPassportView.as_view(),
        name= 'get-passport'
    ),
    path(
        '<student_id>/citizenship/get',
        views.GetCitizenshipView.as_view(),
        name='get-passport'
    )
]
