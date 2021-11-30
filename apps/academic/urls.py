from django.urls import path

from apps.academic import views

urlpatterns = [
    path(
        '<student_id>/add',
        views.CreateAcademicView.as_view(),
        name = 'add-academic-detail'
    )
]
