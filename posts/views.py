from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def get_posts(request):
    public_posts = Post.objects.filter(visibility=Post.Status.PUBLIC)
    private_posts_community = Post.objects.filter(visibility=Post.Status.PRIVATE)

    all_posts = public_posts | private_posts_community
    all_posts = all_posts.order_by('created_at')  

    serialized_data = PostSerializer(all_posts, many=True).data
    return Response(serialized_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_post_by_id(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return Response({'message': 'Post berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)
