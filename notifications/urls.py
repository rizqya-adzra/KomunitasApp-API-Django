from django.urls import path
from .views import get_notifications, create_notification

urlpatterns = [
    path('notifications/', get_notifications, name='get_notifications'),
    path('notifications/create', create_notification, name='create_notification')
]
