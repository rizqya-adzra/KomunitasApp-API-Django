from django.urls import path
from .views import get_chats, create_chat, edit_chat, delete_chat, get_chat_by_id

urlpatterns = [
    path('chats/', get_chats, name='get_chats'),
    path('chats/<int:pk>/', get_chat_by_id, name='get_chat_by_id'),
    path('chats/create/', create_chat, name='create_chat'),
    path('chats/edit/<int:pk>/', edit_chat, name='edit_chat'),
    path('chats/delete/<int:pk>/', delete_chat, name='delete_chat')
]   


