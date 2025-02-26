from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request):
    public_posts = Post.objects.filter(visibility=Post.Status.PUBLIC)
    private_posts_community = Post.objects.filter(visibility=Post.Status.PRIVATE)

    all_posts = public_posts | private_posts_community
    all_posts = all_posts.order_by('-created_at')  

    serialized_data = PostSerializer(all_posts, many=True).data
    return Response(serialized_data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post_by_id(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user_id != request.user.id:
        return Response({'message': 'Anda tidak memiliki izin untuk menghapus postingan ini'}, status=status.HTTP_403_FORBIDDEN)
    post.delete()
    return Response({'message': 'Post berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)