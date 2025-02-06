from django.urls import path
from .views import get_communities, create_communities, community_detail, get_community_by_id, delete_image

urlpatterns = [
    path('communities/', get_communities, name='get_communities'),
    path('communities/create', create_communities, name='create_communities'),
    path('communities/<int:pk>', community_detail, name='community_detail'),
    path('communities/detail/<int:pk>', get_community_by_id, name='get_community_by_id'),
    path('communities/delete/<int:pk>', delete_image, name='delete_image'),
]
        