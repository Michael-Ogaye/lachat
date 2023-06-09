from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.Chatconsumer.as_asgi()),
    re_path(r'ws/stocks/$',consumers.StocksConsumer.as_asgi(),name='stocks')
]
