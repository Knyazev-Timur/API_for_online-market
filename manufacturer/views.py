from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from manufacturer.models import Manufacturer
from manufacturer.serializers import ManufacturerListSerializer, ManufacturerDetailSerializer, \
    ManufacturerCreateSerializer, ManufacturerDestroySerializer, ManufacturerUpdateSerializer


class ManufacturerListView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerListSerializer

#
class ManufacturerCreateView(CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerCreateSerializer
#
#
class ManufacturerDetailView(RetrieveAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerDetailSerializer


class ManufacturerUpdateView(UpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerUpdateSerializer


class ManufacturerDeleteView(DestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerDestroySerializer