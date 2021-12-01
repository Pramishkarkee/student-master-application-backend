from django.urls import path

from apps.parentsDetail import views

urlpatterns = [
    path(
        '<student_id>/add',
        views.AddParentsView.as_view(),
        name="add-student-parents-detail"
    )
]
