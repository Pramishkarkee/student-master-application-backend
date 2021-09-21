from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils.timezone import now
from django.views import generic


class ReceiveNotificationView(generic.TemplateView):
    template_name = 'receive.html'


class SendNotificationView(generic.TemplateView):
    template_name = 'send.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        channel_layer = get_channel_layer()
        data = "notification" + "...." + str(now())
        async_to_sync(channel_layer.group_send)(
            str(current_user.pk),
            {
                "type": "notify",
                "text": data,
            },
        )
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
