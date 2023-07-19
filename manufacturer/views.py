from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from manufacturer.models import Manufacturer
from manufacturer.serializers import ManufacturerListSerializer, ManufacturerDetailSerializer, \
    ManufacturerCreateSerializer, ManufacturerDestroySerializer, ManufacturerUpdateSerializer
from users.permissions import UserIsActivePermission


class ManufacturerListView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerListSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ManufacturerCreateView(CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerCreateSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ManufacturerDetailView(RetrieveAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerDetailSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ManufacturerUpdateView(UpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerUpdateSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ManufacturerDeleteView(DestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerDestroySerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]
