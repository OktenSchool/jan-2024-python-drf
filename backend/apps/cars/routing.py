from django.urls import path

from apps.cars.consumers import CarConsumer

websocket_urlpatterns = [
    path('', CarConsumer.as_asgi()),
]
