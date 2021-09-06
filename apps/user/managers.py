from django.contrib.auth.base_user import BaseUserManager


class StudentUserManager(BaseUserManager):
    def get_queryset(self):
        return super(StudentUserManager, self).get_queryset().filter(
            user_type='student_user'
        )


class InstituteUserManager(BaseUserManager):
    def get_queryset(self):
        return super(InstituteUserManager, self).get_queryset().filter(
            user_type='institute_user'
        )


class ConsultancyUserManager(BaseUserManager):
    def get_queryset(self):
        return super(ConsultancyUserManager, self).get_queryset().filter(
            user_type='consultancy_user'
        )


class PortalUserManager(BaseUserManager):
    def get_queryset(self):
        return super(PortalUserManager, self).get_queryset().filter(
            user_type='portal_user'
        )
