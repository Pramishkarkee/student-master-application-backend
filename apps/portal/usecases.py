# from django.core.exceptions import ValidationError as DjangoValidationError
# from rest_framework.exceptions import ValidationError
#
# from apps.core import usecases
# from apps.core.usecases import BaseUseCase
# from apps.portal import tasks
# from apps.portal.emails import SendEmailToPortalStaff
# from apps.portal.exceptions import PortalNotFound
# from apps.portal.models import PortalStaff
# from apps.settings.models import Settings
# from apps.staff.models import StaffPosition
# from apps.user.models import PortalUser
#
#
# # class RegisterPortalUseCase(usecases.CreateUseCase):
# #     def _factory(self):
# #         # 1. create portal user
# #         user = PortalUser.objects.create(
# #             email=self._data.pop('email'),
# #             password=self._data.pop('password')
# #         )
# #         # 2. consultancy
# #         portal = Portal.objects.create(
# #             **self._data
# #         )
# #         staff_position, created = StaffPosition.objects.get_or_create(name='owner')
# #         # 3. consultancy staff
# #         settings = Settings.objects.create(user=user)
# #
# #         staff = PortalStaff.objects.create(
# #             user=user,
# #             portal=portal,
# #             position=staff_position
# #         )
#
#
# class GetPortalUseCase(BaseUseCase):
#     def __init__(self, portal_id: Portal):
#         self._portal_id = portal_id
#
#     def execute(self):
#         self._factory()
#         return self._portal
#
#     def _factory(self):
#         try:
#             self._portal = Portal.objects.get(pk=self._portal_id)
#         except Portal.DoesNotExist:
#             raise PortalNotFound
#
#
# class CreatePortalStaffUseCase(usecases.CreateUseCase):
#     def __init__(self, serializer, portal):
#         self._portal = portal
#         super().__init__(serializer)
#
#     def execute(self):
#         self._factory()
#
#     def _factory(self):
#         user = {
#             'email': self._data.pop('email'),
#             'fullname': self._data.pop('fullname'),
#         }
#         # 1. create consultancy user
#         portal_user = PortalUser.objects.create(
#             **user
#         )
#         settings = Settings.objects.create(user=portal_user)
#
#         # 2. portal staff
#         try:
#             portal_staff = PortalStaff.objects.create(
#                 user=portal_user,
#                 portal=self._portal,
#                 role=self._data['role']
#             )
#             portal_staff.clean()
#         except DjangoValidationError as e:
#             raise ValidationError(e.message_dict)
#
#         context = {
#             'uuid': portal_user.id,
#             'name': self._portal.name,
#             'user_email': portal_user.email,
#         }
#         tasks.send_set_password_email_to_user.apply_async(
#             kwargs=context
#         )
#
#         # without celery
#         # SendEmailToPortalStaff(
#         #     context={
#         #         'uuid': portal_user.id,
#         #         'name': self._portal.name,
#         #     }
#         # ).send(to=[portal_user.email])
