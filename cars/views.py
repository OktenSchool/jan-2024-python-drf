from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin

from cars.filter import car_filter
from cars.models import CarModel
from cars.serializers import CarSerializer


# class CarListCreateView(GenericAPIView):
#     def get(self, *args, **kwargs):
#         # qs = CarModel.objects.filter(brand__in=['bmw', 'opel'], year=1987)
#         # qs = CarModel.objects.filter(Q(brand__in=['bmw', 'opel']) | Q(price=2000)).exclude(brand='bmw').count()
#         # qs = CarModel.objects.filter(Q(brand__in=['bmw', 'opel']) | Q(price=2000)).order_by('-price' , 'brand').reverse()
#         # qs = CarModel.objects.filter(Q(brand__in=['bmw', 'opel']) | Q(price=2000)).values('id', 'brand')
#         # qs = CarModel.objects.all()[2:4]
#         # print(qs.query)
#         # res = [model_to_dict(car) for car in cars]
#         qs = CarModel.objects.all()
#         serializer = CarSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found")
#         car = self.get_object()
#         serializer = CarSerializer(car, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             return Response("not found")
#         serializer = CarSerializer(car, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         #     car.delete()
#         # except CarModel.DoesNotExist:
#         #     return Response("not found")
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#     def get_queryset(self):
#         return car_filter(self.request.query_params)
#
#     # def get_serializer(self, *args, **kwargs):
#     #     return super().get_serializer(*args, **kwargs)
#     #
#     # def get_object(self):
#     #     return super().get_object()
#
#
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
