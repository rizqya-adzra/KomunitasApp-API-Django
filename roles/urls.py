from django.urls import path
from .views import get_roles, create_roles

urlpatterns = [
    path('roles/', get_roles, name='get_roles'),
    path('roles/create', create_roles, name='create_roles')
]
