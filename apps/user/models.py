import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from apps.user.utils import upload_normal_user_avatar_to
from apps.user.validators import validate_username


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        _('email address'),
        unique=True
    )
    fullname = models.CharField(_('fullname'), max_length=200, null=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[validate_username],
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_archived = models.BooleanField(default=False)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["fullname", "email"]
    objects = UserManager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super(User, self).save(*args, **kwargs)

    def activate(self):
        self.is_active = True
        self.save(update_fields=['is_active'])


class BaseUser(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username


class NormalUser(BaseUser):
    avatar = models.ImageField(
        upload_to=upload_normal_user_avatar_to,
        blank=True,
        default='avatar/avatar_default.jpg'
    )

    def clean(self):
        # only user allowed
        if self.user.is_staff or self.user.is_superuser:
            raise DjangoValidationError({
                'user': _('User is not a normal user.')
            })
