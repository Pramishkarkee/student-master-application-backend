from django.shortcuts import render

# Create your views here.
from apps.core import generics
from apps.gallery import serializers, usecases
from apps.gallery.mixins import GalleryMixin
from django.utils.translation import gettext_lazy as _


class AddGalleryView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to add gallery
    """
    serializer_class = serializers.AddGallerySerializer
    message = 'Created successfully'

    def perform_create(self, serializer):
        return usecases.AddGalleryUseCase(serializer=serializer).execute()


class ListGalleryView(generics.ListAPIView):
    """
    Use this end-point to List  all  blogs
    """
    serializer_class = serializers.ListGallerySerializer
    no_content_error_message = _('No gallery at the moment')

    def get_queryset(self):
        return usecases.ListGalleryUseCase().execute()


class DeleteGalleryView(GalleryMixin, generics.DestroyAPIView):
    """
    Use this endpoint to delete gallery
    """

    def get_object(self):
        return self.get_gallery()

    def perform_destroy(self, instance):
        return usecases.DeleteGalleryUseCase(
            gallery=self.get_object(),
        ).execute()


class UpdateGalleryView(generics.UpdateAPIView, GalleryMixin):
    """
    Use this end-point to Update   blogs.
    """

    serializer_class = serializers.UpdateGallerySerializer
    queryset = ''


    def get_object(self):
        return self.get_gallery()

    def perform_update(self, serializer):
        return usecases.UpdateGalleryUseCase(
            serializer=serializer,
            gallery=self.get_object()
        ).execute()
