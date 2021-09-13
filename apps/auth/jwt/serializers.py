from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils.datetime_safe import datetime
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.serializers import (
    TokenObtainSerializer,
    TokenRefreshSerializer,
    PasswordField
)
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from apps.auth.jwt.cache import LoginCache
from apps.pyotp.mixins import OTPMixin

User = get_user_model()


class CustomTokenObtainSerializer(TokenObtainSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'] = PasswordField()

    def validate(self, attrs):
        cache_results = LoginCache.get(attrs['username'])
        lockout_timestamp = None
        invalid_attempt_timestamps = cache_results['invalid_attempt_timestamps'] if cache_results else []

        invalid_attempt_timestamps = [timestamp for timestamp in invalid_attempt_timestamps if
                                      timestamp > (datetime.now() - timedelta(minutes=15))]

        if len(invalid_attempt_timestamps) >= 5:
            raise serializers.ValidationError(
                _('too many attempts, account locked ! wait for 15 minutes'),
            )

        self.user = self.authenticate(username=attrs['username'], password=attrs['password'])

        if self.user is None:
            invalid_attempt_timestamps.append(datetime.now())
            if len(invalid_attempt_timestamps) >= 5:
                lockout_timestamp = datetime.now()
                raise serializers.ValidationError(
                    _('locked.')
                )
            LoginCache.set(attrs['username'], invalid_attempt_timestamps, lockout_timestamp)
            raise serializers.ValidationError(
                _('Email or Password does not matched .'),
            )
        if self.user:
            if not self.user.is_active:
                msg = _('User account is not activated.')
                raise PermissionDenied(msg)

            if self.user.is_archived:
                msg = _('User is archived.')
                raise PermissionDenied(msg)
        LoginCache.delete(attrs['username'])
        return {}

    def authenticate(self, username, password):
        try:
            user = User.objects.get(
                Q(email=username) | Q(username=username)
            )
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            User().set_password(password)


class LoginSerializer(CustomTokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        self.validate_user()
        refresh = self.get_token(self.user)

        data['refresh_token'] = str(refresh)
        data['token'] = str(refresh.access_token)

        self.user.last_login = now()
        self.user.save()
        return data

    def validate_user(self):
        pass


class NormalUserLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        data = super(NormalUserLoginSerializer, self).validate(attrs)
        # user detail
        data['user'] = self.user
        return data


# class ConsultancyUserLoginSerializer(LoginSerializer):
#     def validate_user(self):
#         if self.user.user_type != 'consultancy_user':
#             raise serializers.ValidationError(
#                 _('Email or Password does not matched.'),
#             )


class ConsultancyUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = PasswordField()


class ResendOTPCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    default_error_messages = {
        'invalid_email': _('Invalid email.')
    }

    def validate_email(self, value):
        try:
            self.user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(self.fail('invalid_email'))
        return value


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)


class VerifyConsultanyUserOTPSerializer(CodeSerializer, OTPMixin):
    """
    Use this to activate any user
    """

    def get_token(self, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        attrs = super(VerifyConsultanyUserOTPSerializer, self).validate(attrs)
        # get current user from views
        user = self.context['view'].get_object()
        # check for otp code validation
        is_code_valid = self.verify_otp_for_user(user, attrs['code'], '2FA')
        if is_code_valid:
            data = super().validate(attrs)
            refresh = self.get_token(user)
            data['refresh_token'] = str(refresh)
            data['token'] = str(refresh.access_token)
            user.last_login = now()
            user.save()
            return data
        else:
            raise serializers.ValidationError(
                {'code': _('Invalid code.')}
            )


class CustomTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        data = {'token': str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()

            data['refresh_token'] = str(refresh)

        return data


class NormalUserLoginDetailSerializer(serializers.Serializer):
    fullname = serializers.CharField()
    avatar = serializers.ImageField(source='normaluser.avatar')


class NormalUserLoginResponseSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)
    user_detail = NormalUserLoginDetailSerializer(source='user', read_only=True)


class ConsultancyUserLoginResponseSerializer(NormalUserLoginResponseSerializer):
    user_detail = None
