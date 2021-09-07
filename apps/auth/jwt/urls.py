from django.urls import path
from rest_framework_simplejwt.views import token_verify

from apps.auth.jwt import views

urlpatterns = [
    path(
        'consultancy-user/login',
        views.ConsultancyUserLoginView.as_view(),
        name='consultancy-user-login'
    ),
    path(
        'login-refresh',
        views.CustomTokenRefreshView.as_view(),
        name='login-refresh'
    ),
    path(
        'login-verify',
        token_verify,
        name='login-verify'
    ),
]
