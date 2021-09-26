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

    path(
        'user/<user_id>/create-password',
        views.CreatePasswordForConsultancyUserView.as_view(),
        name='create-password-for-consultancy-staff'
    ),
    path(
        '<consultancy_id>/list',
        views.ListConsultancyStaffView.as_view(),
        name='list-consultancy-staff'
    ),
    path(
        'consultancy_staff/<consultancy_staff_id>/update',
        views.UpdateConsultancyStaffView.as_view(),
        name='update-consultancy-staff'
    ),
    path(
        'list',
        views.ListConsultancyView.as_view(),
        name='list-consultancy'
    ),

]
