from apps.institute.models import Institute
from apps import institute
from apps.institute.mixins import InstituteMixins, ScholorshipMixins, SocialMediaMixins
from apps.studentIdentity import usecases
from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.permissions import AllowAny

from apps.institute import serializers
from apps.core import generics
from apps.institute import usecase
from apps.institute import usecase
# Create your views here.

class RegisterInstituteView(generics.CreateWithMessageAPIView):
    """
    use this endpoint to register consultancy
    """
    parser_classes = (MultiPartParser,FileUploadParser)
    message = _('Register successfully')
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterInstituteSerializer

    def perform_create(self, serializer):
        return usecase.RegisterInstituteUsecase(
            serializer=serializer
        ).execute()

class AddInstituteStaffView(generics.CreateWithMessageAPIView ,InstituteMixins):
    """
    This endpoint is use to add staff in institute
    """
    message = 'Institute stsff create successfully'
    serializer_class = serializers.CreateInstituteStaffSerializer
    parser_classes = (MultiPartParser,FileUploadParser)
    message = _('Add staff successfully')

    def get_object(self):
        return self.get_institute()

    def perform_create(self, serializer):
        return usecase.CreateConsultancyStaffUseCase(
            institute=self.get_object(),
            serializer = serializer
        ).execute()

class UpdateInstituteView(generics.UpdateWithMessageAPIView,InstituteMixins):
    """
    This endpoint is use to update institute
    """
    message = 'institute update successfully'
    serializer_class = serializers.UpdateInstituteSerializer
    

    def get_object(self):
        return self.get_institute()

    def perform_update(self, serializer):
        return usecase.UpdateInstituteUseCase(
            institute=self.get_object(),
            serializer = serializer
        ).execute()
#update logo
class UpdateInstituteLogoView(generics.UpdateWithMessageAPIView,InstituteMixins):
    """
    This endpoint is use to update institute logo
    """
    message = 'institute logo update successfully'
    serializer_class = serializers.UpdateInstituteLogoSerializer
    parser_classes = (MultiPartParser,FileUploadParser)
    def get_object(self):
        return self.get_institute()

    def perform_update(self, serializer):
        return usecase.UpdateInstituteUseCase(
            institute=self.get_object(),
            serializer = serializer
        ).execute()

#update coverimage
class UpdateInstituteCoverimageView(generics.UpdateWithMessageAPIView,InstituteMixins):
    """
    This endpoint is use to update institute coverimage
    """
    message = 'institute coverimage update successfully'
    serializer_class = serializers.UpdateInstituteCoverImageSerializer
    parser_classes = (MultiPartParser,FileUploadParser)

    def get_object(self):
        return self.get_institute()

    def perform_update(self, serializer):
        return usecase.UpdateInstituteUseCase(
            institute=self.get_object(),
            serializer = serializer
        ).execute()


class ListInstituteView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ListInstituteSerializer
    def get_queryset(self):
        return usecase.ListInstituteUseCase().execute()


class DetailInstituteView(generics.RetrieveAPIView,Institute,InstituteMixins):
    """
    this endpoint is use to get institute detail
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.InstituteDetailSerilaizer

    def get_object(self):
        return self.get_institute()

    def get_queryset(self):
        return usecase.GetInstituteDetailUseCase(
            institute_id=self.get_object()
        ).execute()

 
class AddScholorshipView(generics.CreateWithMessageAPIView,InstituteMixins):
    """
    This endpoint is use to add scholorship
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.AddScholorshipSerializer
    message = "Add scholorship successfully"
    def get_object(self):
        return self.get_institute()

    def perform_create(self, serializer):
        return usecase.AddScholorshipUseCase(
            institute = self.get_object(),
            serializer =serializer
        ).execute()


class GetScholorshipListView(generics.ListAPIView,InstituteMixins):
    """
    this endpoint is use to get scholorship
    """
    serializer_class = serializers.GetScholorshipSerializer
    permission_classes = (AllowAny,)
    no_content_error_message = _('No scholorship at this moment')
    def get_object(self):
        return self.get_institute()

    def get_queryset(self):
        return usecase.ListScholorshipUseCase(
            institute = self.get_object()
        ).execute()
        
class UpdateScholorshipView(generics.UpdateWithMessageAPIView,ScholorshipMixins):
    """
    This endpoint is use to update scholorship
    """
    serializer_class = serializers.AddScholorshipSerializer
    message =_("update successfullt")
    def get_object(self):
        return self.get_scholorship()

    def perform_update(self, serializer):
        return usecase.UpdateScholorshipUseCase(
            scholorship=self.get_object(),
            serializer=serializer
        ).execute()
#  AddScholorshipSerializer
class DeleteScholorshipView(generics.DestroyWithMessageAPIView,ScholorshipMixins):
    """
    This endpoint is use to delete scholorship
    """
    message =_("delete successfully")
    def get_object(self):
        return self.get_scholorship()

    def perform_destroy(self, instance):
        return usecase.DeleteScholorshipUseCase(
            scholorship=self.get_object()
        ).execute()


class AddSolicalMediaView(generics.CreateWithMessageAPIView,InstituteMixins):
    """
    this endpoint is use to add sociali media
    """
    message = _("social media added")
    serializer_class = serializers.AddSocialMediaSerializer
    def get_object(self):
        return self.get_institute()

    def perform_create(self, serializer):
        return usecase.SocialiMedialinkUseCase(
            institute=self.get_object(),
            serializer=serializer
        ).execute()


class DeleteSocialMediaView(generics.DestroyWithMessageAPIView,SocialMediaMixins):
    """
    This endpont is use to delete social media
    """
    message = _("social media delete successfully")

    def get_object(self):
        return self.get_socialmedia()

    def perform_destroy(self, instance):
        return usecase.DeleteSocialMediaUseCase(
            socialmedia= self.get_object()
        ).execute()

class GetSocialMediaListView(generics.ListAPIView,InstituteMixins):
    """
    This api is use to get social media link
    """
    serializer_class = serializers.GetSocialMediaSerializer

    def get_object(self):
        return self.get_institute()

    def get_queryset(self):
        return usecase.GetSocialMediaLinkListUseCase(
            institute=self.get_object()
        ).execute()
