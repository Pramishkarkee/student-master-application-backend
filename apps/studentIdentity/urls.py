from django.urls import path
from apps.studentIdentity import views

urlpatterns = [
    path(
        '<student_id>/add',
        views.AddCitizenshipView.as_view(),
        name = 'add citizenship'
    ),
]
