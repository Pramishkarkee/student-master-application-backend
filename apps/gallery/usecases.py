from django.utils.datetime_safe import datetime
from rest_framework.exceptions import ValidationError

from apps.core.usecases import BaseUseCase
from apps.gallery.models import Gallery

from  django.utils.translation import  gettext_lazy as _
class AddGalleryUseCase(BaseUseCase):
    def __init__(self,
                 serializer):
        self.serializer = serializer
        self.data = serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        self._gallery = Gallery(**self.data)
        self._gallery.save()


class ListGalleryUseCase(BaseUseCase):

    def execute(self):
        self._factory()
        return self._gallery

    def _factory(self):
        self._gallery = Gallery.objects.all()


class GetGalleryUseCase(BaseUseCase):
    def __init__(self, gallery_id):
        self._gallery_id = gallery_id

    def execute(self):
        self._factory()
        return self.gallery

    def _factory(self):
        try:
            self.gallery = Gallery.objects.get(pk=self._gallery_id)
        except Gallery.DoesNotExist:
            raise ValidationError({'error': _('Gallery  does not exist for following id.')})


class UpdateGalleryUseCase(BaseUseCase):
    def __init__(self, serializer, gallery: Gallery):
        self.serializer = serializer
        self._data = serializer.validated_data
        self._gallery = gallery

    def execute(self):
        self._factory()

    def _factory(self):
        for key in self._data.keys():
            setattr(self._gallery, key, self._data.get(key))
        self._gallery.updated_at = datetime.now()
        self._gallery.save()


class DeleteGalleryUseCase(BaseUseCase):
    def __init__(self, gallery):
        self._gallery = gallery

    def execute(self):
        self._factory()

    def _factory(self):
        self._gallery.delete()
