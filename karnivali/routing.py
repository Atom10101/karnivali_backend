from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import GameRoom
from .consumers_rps import RPS
from django.urls import re_path

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(URLRouter([
            re_path('ws/game/<room_code>', GameRoom),
            re_path('ws/game/rps/<room_code>', RPS)
        ]))
    }
)