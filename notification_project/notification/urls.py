from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ClientViewSet, NewsletterViewSet, MessageViewSet

app_name = 'notification'

router = DefaultRouter()

router.register('client', ClientViewSet)
router.register('newsletter', NewsletterViewSet)
router.register('message', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]