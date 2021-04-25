"""
Similar to urls.py for HTTP endpoints. This links the ChatConsumer class to the specified chat URL.
"""
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # path('ws/chat/<uuid:room_name>/', consumers.ChatConsumer.as_asgi())
]
