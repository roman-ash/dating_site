from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ClientViewSet


app_name = 'notification'

#router = DefaultRouter()

urlpatterns = [
    #path(include(router.urls)),
    path('client/', ClientViewSet.as_view())
]
