from apps.gallery.usecases import GetGalleryUseCase


class GalleryMixin:
    def get_gallery(self):
        return GetGalleryUseCase(
            gallery_id=self.kwargs.get('gallery_id')
        ).execute()
