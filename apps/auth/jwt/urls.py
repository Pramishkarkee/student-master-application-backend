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
        'portal-user/login',
        views.PortalUserLoginView.as_view(),
        name='portal-user-login'
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
    path(
        'consultancy-user/<str:user_id>/2fa/verify',
        views.ConsultancyUser2FAVerifyView.as_view(),
        name='consultancy-user-2fa-verify'
    ),
    path(
        'portal-user/<str:user_id>/2fa/verify',
        views.PortalUser2FAVerifyView.as_view(),
        name='portal-user-2fa-verify'
    ),
    path(
        'consultancy-user/resend-otp',
        views.ResendOTPCodeView.as_view(),
        name='consultancy-user-resend-otp'
    ),
]
