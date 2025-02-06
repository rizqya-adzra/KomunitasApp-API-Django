from django.urls import path
from .views import get_posts, create_post, edit_post, delete_post, get_post_by_id

urlpatterns = [
    path('posts/', get_posts, name='get_posts'),
    path('posts/<int:pk>/', get_post_by_id, name='get_post_by_id'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/edit/<int:pk>/', edit_post, name='edit_post'),
    path('posts/delete/<int:pk>/', delete_post, name='delete_post')
]   


