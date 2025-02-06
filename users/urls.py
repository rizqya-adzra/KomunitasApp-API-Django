from django.urls import path
from .views import get_users, user_detail, register_user, user_login, user_logout, get_user_by_id

urlpatterns = [
    path('users/login/', user_login, name='login'),
    path('users/logout/', user_logout, name='logout'),
    path('users/register/', register_user, name='register_user'),
    path('users/', get_users, name='get_user'),
    path('users/detail/<int:pk>/', user_detail, name='user_detail'),
    path('users/profile/', get_user_by_id, name='get_user_by_id'),
    # path('users/token', custom_auth_token, name='custom_auth_token')
]
