from django.shortcuts import render

from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer, \
    ProductUpdateSerializer, ProductDestroySerializer
from users.permissions import UserIsActivePermission


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


#
class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


#
#
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDestroySerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]
