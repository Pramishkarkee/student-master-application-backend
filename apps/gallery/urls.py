from django.urls import path

from apps.gallery import views

urlpatterns = [
    path(
        'add',
        views.AddGalleryView.as_view(),
        name='add-gallery'
    ),
    path(
        'list',
        views.ListGalleryView.as_view(),
        name='list-gallery'
    ),
    path(
        '<str:gallery_id>/update',
        views.UpdateGalleryView.as_view(),
        name='update-gallery'

    ),
    path(
        '<str:gallery_id>/delete',
        views.DeleteGalleryView.as_view(),
        name='delete-gallery'

    )
]