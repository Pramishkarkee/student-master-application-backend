from django.urls import path

from apps.academic import views

urlpatterns = [
    path(
        '<student_id>/institute-education/add',
        views.CreateAcademicView.as_view(),
        name = 'add-academic-detail'
    ),
    path(
        '<student_id>/sop/add',
        views.CreateSopView.as_view(),
        name = 'add-sop'
    ),
    path(
        '<student_id>/lor/add',
        views.CreateLorView.as_view(),
        name= 'add-lor'
    ),
    path(
        '<student_id>/personal-essay/add',
        views.CreatePersonalEssayView.as_view(),
        name = 'add-essay'
    )
]
