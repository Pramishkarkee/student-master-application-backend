from django.urls import path
from apps.institute import views

from apps.institute.views import RegisterInstituteView

urlpatterns = [
    path(
        'reguster',
        views.RegisterInstituteView.as_view(),
        name='register-institute'
    )
]
