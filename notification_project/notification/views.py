from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from .models import Client, Newsletter, Message
from .serializers import ClientSerializer, NewsletterSerializer, MessageSerializer


class ClientViewSet(viewsets.GenericViewSet,
                      generics.CreateAPIView,
                      generics.ListAPIView,
                      generics.RetrieveAPIView,
                      generics.UpdateAPIView,
                      generics.DestroyAPIView):  # viewsets.ModelViewSet
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class NewsletterViewSet(viewsets.GenericViewSet,
                      generics.CreateAPIView,
                      generics.ListAPIView,
                      generics.RetrieveAPIView,
                      generics.UpdateAPIView,
                      generics.DestroyAPIView):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()


class MessageViewSet(viewsets.GenericViewSet,
                      generics.CreateAPIView,
                      generics.ListAPIView,
                      generics.RetrieveAPIView,
                      generics.UpdateAPIView,
                      generics.DestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
