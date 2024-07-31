from django.urls import path

from apps.cars.views import CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),
]
