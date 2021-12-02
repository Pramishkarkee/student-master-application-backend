from django.urls import path

from apps.academic import views

urlpatterns = [
    path(
        '<student_id>/institute-education/add',
        views.CreateAcademicView.as_view(),
        name = 'add-academic-detail'
    ),
    path(
        '<student_id>/institute-education/list',
        views.GetAcademicListView.as_view(),
        name = 'academic-list'
    ),
    path(
        '<academic_id>/institute-education/update',
        views.UpdateAcademicView.as_view(),
        name = 'academic-update'
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
        '<student_id>/sop/get',
        views.GetSopView.as_view(),
        name='get-sop'
    ),
    path(
        '<student_id>/lor/list',
        views.GetLorListView.as_view(),
        name="list-lor"
    ),
    path(
        '<student_id>/personal-essay/add',
        views.CreatePersonalEssayView.as_view(),
        name = 'add-essay'
    ),
    path(
        '<student_id>/personal-essay/get',
        views.GetEssayView.as_view(),
        name = 'get-essay'
    ),
]
