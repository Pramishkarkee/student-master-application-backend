from datetime import timedelta

from django.contrib.auth import get_user_model, authenticate
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError, PermissionDenied

from apps.auth.jwt.emails import EmailVerificationEmail
from apps.core.usecases import CreateUseCase
from apps.pyotp.mixins import OTPMixin
from apps.pyotp.models import PyOTP

User = get_user_model()


class ConsultancyUserLoginWithOTPUseCase(CreateUseCase, OTPMixin):
    def __init__(self, request, serializer):
        self._request = request
        super().__init__(serializer)

    def execute(self):
        self._factory()

    def _factory(self):
        credentials = {
            'username': self._data['email'],
            'password': self._data['password']
        }
        print(credentials)
        self._user = authenticate(self._request, **credentials)
        print(self._user)
        if self._user is not None:
            """
            Sends email confirmation mail to the user's email
            :return: None
            """
            code = self._generate_totp(
                user=self._user,
                purpose='2FA',
                interval=180
            )
            print(code)

            EmailVerificationEmail(
                context={
                    'code': code,
                    'uuid': self._user.id
                }
            ).send(to=[self._user.email])
        else:
            raise PermissionDenied(
                {
                    'authentication_error': _('User name or password not matched')
                }
            )


class ResendOTPCodeUseCase(CreateUseCase, OTPMixin):
    """
    Use this endpoint to resend otp
    """

    def __init__(self, serializer):
        self._serializer = serializer
        self._user = self._serializer.user
        super().__init__(self._serializer)

    def execute(self):
        self.is_valid()
        self._factory()

    def is_valid(self):
        # wait for 2 minutes.
        try:
            old_otp = PyOTP.objects.get(
                user=self._user,
                purpose='2FA'
            )
        except PyOTP.DoesNotExist:
            raise ValidationError({
                'non_field_errors': _('Has no old OTP')
            })

        if old_otp.created_at + timedelta(minutes=2) > timezone.now():
            raise ValidationError({
                'non_field_errors': _('OTP Resend  can be performed only after 2 minutes.')
            })

    def _factory(self):
        code = self._regenerate_totp(self._user, '2FA')
        print(code)
        EmailVerificationEmail(
            context={
                'code': code,
                'uuid': self._user.id
            }
        ).send(to=[self._user.email])
