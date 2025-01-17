from django.urls import path
from .views import get_communities, create_communities, community_detail

urlpatterns = [
    path('communities/', get_communities, name='get_communities'),
    path('communities/create', create_communities, name='create_communities'),
    path('communities/<int:pk>', community_detail, name='community_detail'),
]
        