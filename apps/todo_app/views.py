from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def car_list(request):
    queryset = Car.objects.all()
    serializer = CarSerializer(queryset, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response( 'Машина успешно создана', status=200)

@api_view(['PATCH'])
def update_car(request, id):
    car = get_object_or_404(Car, id = id)
    serializer = CarSerializer(car, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Машина успешно обновлена', status=201)

@api_view(['DELETE'])
def delete_car(request, id):
    car = get_object_or_404(Car, id=id)
    car.delete()
    return Response('Машина успешно удалена', status=204)
