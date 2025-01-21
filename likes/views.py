from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Like
from .serializers import LikeSerializer

# @api_view(['GET'])
# def get_likes(request):
#     likes = Like.objects.all()
#     serializerData = LikeSerializer(likes, many=True).data
#     return Response(serializerData, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_likes(request):
    post = request.query_params.get('post')  
    if not post:
        return Response({"error": "post_id nya tidak masuk"}, status=status.HTTP_400_BAD_REQUEST)
    likes = Like.objects.filter(post=post) 
    serializerData = LikeSerializer(likes, many=True).data
    return Response(serializerData, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_like(request):
    data = request.data
    serializer = LikeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 