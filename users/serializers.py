from rest_framework import serializers
from .models import User
from roles.models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role', 'community']

class UserSerializer(serializers.ModelSerializer):
    role_detail = serializers.SerializerMethodField()  

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role_detail', 'bio', 'profile_photo', 'created_at']  

    def get_role_detail(self, obj):
        roles = Role.objects.filter(user=obj)  
        return RoleSerializer(roles, many=True).data 
