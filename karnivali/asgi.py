"""
ASGI config for karnivali project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karnivali.settings')
django.setup()
application = get_default_application()


#import os
#from django.core.asgi import get_asgi_application
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karnivali.settings')
#application = get_asgi_application()




#application = ProtocolTypeRouter(
#    {
 #       'websocket': AuthMiddlewareStack(URLRouter([
 #           path('ws/game/<room_code>', GameRoom),
 #           path('ws/game/rps/<room_code>', RPS)
 #       ]))
 #   },
    # {
    #     'websocket': AuthMiddlewareStack(URLRouter([
    #         path('ws/game/rps/<room_code>', RPS)
    #     ]))
    # }
#)
