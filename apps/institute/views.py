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

 