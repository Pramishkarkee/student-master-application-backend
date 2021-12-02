from django.urls import path
from apps.institute import views

from apps.institute.views import RegisterInstituteView

urlpatterns = [
    path(
        'register',
        views.RegisterInstituteView.as_view(),
        name='register-institute'
    ),
    path(
        'inistitutelist',
        views.ListInstituteView.as_view(),
        name = 'institute-list'
    )
]
