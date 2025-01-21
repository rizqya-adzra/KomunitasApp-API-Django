from django.urls import path
from .views import get_bookmarks, create_bookmark

urlpatterns = [
    path('bookmarks/', get_bookmarks, name='get_bookmarks'),
    path('bookmarks/create', create_bookmark, name='create_bookmark')
]
