from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(generics.CreateAPIView,
                      generics.ListAPIView,
                      generics.RetrieveAPIView,
                      generics.UpdateAPIView,
                      generics.DestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
