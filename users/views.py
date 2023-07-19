from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import UserIsActivePermission
from users.serializers import UserCreateSerializer, UserListSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]