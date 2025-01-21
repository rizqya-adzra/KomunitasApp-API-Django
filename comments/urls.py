from django.urls import path
from .views import get_comments, create_comment

urlpatterns = [
    path('comments/', get_comments, name='get_comments'),
    path('comments/create', create_comment, name='create_comment')
]
