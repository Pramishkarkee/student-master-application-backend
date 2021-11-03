from rest_framework import serializers

from apps.gallery.models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class AddGallerySerializer(GallerySerializer):
    class Meta(GallerySerializer.Meta):
        fields = (
            'image',
            'title'

        )


class ListGallerySerializer(GallerySerializer):
    class Meta(GallerySerializer.Meta):
        fields = (
            'id',
            'image',
            'title',
            'created_at',
            'updated_at',
        )


class UpdateGallerySerializer(AddGallerySerializer):
    pass
