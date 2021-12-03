from apps import institute
from apps.institute.mixins import InstituteMixins, ScholorshipMixins
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


class ListInstituteView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ListInstituteSerializer
    def get_queryset(self):
        return usecase.ListInstituteUseCase().execute()

 
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