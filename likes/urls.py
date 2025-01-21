from django.urls import path
from .views import get_likes, create_like

urlpatterns = [
    path('likes/', get_likes, name='get_likes'),
    path('likes/create', create_like, name='create_like')
]
