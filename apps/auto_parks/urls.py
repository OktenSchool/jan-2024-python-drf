from django.urls import path

from apps.auto_parks.views import AutoParkAddCarView, AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view()),
]