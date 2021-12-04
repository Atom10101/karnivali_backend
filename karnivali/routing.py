from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import GameRoom
from .consumers_rps import RPS
from django.urls import re_path

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(URLRouter([
            re_path(r'ws/game/(?P<room_code>\w+)$', GameRoom),
            re_path(r'ws/game/rps/(?P<room_code>\w+)$', RPS)
        ]))
    }
)