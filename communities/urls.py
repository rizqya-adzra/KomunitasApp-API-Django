from django.urls import path
from .views import get_communities, create_communities, community_detail, get_community_by_id, delete_image, join_community, get_community_members, get_joined_communities

urlpatterns = [
    path('communities/', get_communities, name='get_communities'),
    path('communities/create/', create_communities, name='create_communities'),
    path('communities/<int:pk>/', community_detail, name='community_detail'),
    path('communities/detail/<int:pk>/', get_community_by_id, name='get_community_by_id'),
    path('communities/delete/<int:pk>/', delete_image, name='delete_image'),
    path('communities/join/<int:pk>/', join_community, name='join_community'),
    path('communities/<int:pk>/members/', get_community_members, name='get_community_members'),
    path('communities/joined/', get_joined_communities, name='get_joined_communities')
]
        