from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from contacts.models import Contact
from contacts.serializers import ContactListSerializer, ContactCreateSerializer, ContactDetailSerializer, \
    ContactUpdateSerializer, ContactDestroySerializer
from users.permissions import UserIsActivePermission


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ContactDetailView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ContactUpdateView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactUpdateSerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class ContactDeleteView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDestroySerializer
    permission_classes = [IsAuthenticated, UserIsActivePermission]
