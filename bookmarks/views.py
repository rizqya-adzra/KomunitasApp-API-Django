from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bookmark
from .serializers import BookmarkSerializer

@api_view(['GET'])
def get_bookmarks(request):
    bookmarks = Bookmark.objects.all()
    serializerData = BookmarkSerializer(bookmarks, many=True).data
    return Response(serializerData, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_bookmark(request):
    data = request.data
    serializer = BookmarkSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 