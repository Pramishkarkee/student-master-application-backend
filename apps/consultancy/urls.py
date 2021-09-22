from django.urls import path

from apps.consultancy import views

urlpatterns = [
    path(
        'register',
        views.RegisterConsultancyView.as_view(),
        name='register-consultancy'
    ),
    path(
        '<consultancy_id>/add-staff',
        views.CreateConsultancyStaffView.as_view(),
        name='create-consultancy-staff'
    ),

]
