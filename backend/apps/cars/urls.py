from django.urls import path

from apps.cars.views import CarListView

urlpatterns = [
    path('', CarListView.as_view()),
    # path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),
    # path('/<int:pk>/photo', CarAddPhotoView.as_view()),
    # path('/test', TestEmailView.as_view())
]
