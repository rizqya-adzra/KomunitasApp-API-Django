from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializers

@api_view(['GET'])
def get_notifications(request):
    notification = Notification.objects.all()
    serializedData = NotificationSerializers(notification, many=True).data
    return Response(serializedData, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def create_notification(request):
    data = request.data
    serializer = NotificationSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 