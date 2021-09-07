from django.urls import path

from apps.consultancy import views

urlpatterns = [
    path(
        'register',
        views.RegisterConsultancyView.as_view(),
        name='register-consultancy'
    ),
]
