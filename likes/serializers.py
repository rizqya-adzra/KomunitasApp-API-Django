from rest_framework import serializers
from .models import Like

class Like(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'