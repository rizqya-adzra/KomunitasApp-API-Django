from rest_framework import serializers
from .models import Post
from users.models import User
from communities.models import Community

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_photo']

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    user_detail = UserSerializer(source='user', read_only=True) 
    community = serializers.PrimaryKeyRelatedField(queryset=Community.objects.all(), write_only=True)
    community_detail = CommunitySerializer(source='community', read_only=True)  

    class Meta:
        model = Post
        fields = '__all__' 
        fields = ['id', 'user', 'user_detail', 'community', 'community_detail', 'description', 'image', 'attachment', 'visibility', 'created_at']

