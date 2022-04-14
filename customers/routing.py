from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path(r"ws/teller-view/(?P<pk>\w+)/$",
            consumer.CustomerConsumer.as_asgi())
]
