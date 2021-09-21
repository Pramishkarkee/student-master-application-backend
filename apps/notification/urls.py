from django.urls import path

from apps.notification import views

urlpatterns = [
    path(
        'receive',
        views.ReceiveNotificationView.as_view(),
        name='receive_notification'
    ),
    path(
        'send',
        views.SendNotificationView.as_view(),
        name='send_notification'
    )
]