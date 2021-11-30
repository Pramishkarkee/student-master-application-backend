from django.urls import path
from apps.studentIdentity import views

urlpatterns = [
    path(
        '<student_id>/citizenship/add',
        views.AddCitizenshipView.as_view(),
        name = 'add citizenship'
    ),
    path(
        '<student_id>/passport/add',
        views.AddPassportView.as_view(),
        name = 'add passport'
    )
]
