from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from contacts.models import Contact
from contacts.serializers import ContactListSerializer, ContactCreateSerializer, ContactDetailSerializer, \
    ContactUpdateSerializer, ContactDestroySerializer


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer


class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer


class ContactDetailView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializer


class ContactUpdateView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactUpdateSerializer


class ContactDeleteView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDestroySerializer