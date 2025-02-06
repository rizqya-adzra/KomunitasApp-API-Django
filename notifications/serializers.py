from rest_framework import serializers
from .models import Notification

class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__' 

    def validate(self, data):
        required_fields = ['post', 'community', 'user']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError({field: f"{field} harus diisi."})
        return data
