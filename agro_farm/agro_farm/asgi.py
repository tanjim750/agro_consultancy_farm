
import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from farm.consumers import chatwith

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agro_farm.settings')

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    "websocket":URLRouter([
                path("", chatwith.as_asgi()),
            ])
})
