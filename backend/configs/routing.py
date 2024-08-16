from django.urls import path

from channels.routing import URLRouter

from apps.cars.routing import websocket_urlpatterns as cars_routing
from apps.chat.routing import websocket_urlpatterns as chat_routing

websocket_urlpatterns = [
    path('api/chat/', URLRouter(chat_routing)),
    path('api/cars/', URLRouter(cars_routing)),

]
