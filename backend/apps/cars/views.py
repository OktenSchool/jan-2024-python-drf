from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from core.permissions.is_super_user_permission import IsSuperUser
from core.services.email_service import EmailService

from apps.cars.filter import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[], operation_summary='create new car', operation_id='dddddddddd'))
class CarListView(ListCreateAPIView):
    """
    Get all cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)
    pagination_class = None
#
#
# class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     """
#     get:
#         get car details
#     put:
#         update car
#     patch:
#         partial update car
#     delete:
#         delete car
#     """
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get_permissions(self):
#         if self.request.method == 'DELETE':
#             return (IsAuthenticated(),)
#         return (AllowAny(),)
#
#
# class CarAddPhotoView(UpdateAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = CarPhotoSerializer
#     queryset = CarModel.objects.all()
#     http_method_names = ('put',)
#
#     def perform_update(self, serializer):
#         car = self.get_object()
#         car.photo.delete()
#         super().perform_update(serializer)
#
#
# # class TestEmailView(GenericAPIView):
# #     permission_classes = (AllowAny,)
# #
# #     def get(self, *args, **kwargs):
# #         EmailService.send_test()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
