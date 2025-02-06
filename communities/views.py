from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Community
from .serializers import CommunitySerializer

@api_view(['GET'])
def get_communities(request):
    communities = Community.objects.all()
    serializedData = CommunitySerializer(communities, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_communities(request):
    data = request.data
    serializer = CommunitySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    detailed_errors = {}
    for field, errors in serializer.errors.items():
        detailed_errors[field] = ", ".join(errors)
    
    return Response(
        {
            "message": "Data tidak valid.",
            "errors": detailed_errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['PUT', 'DELETE'])
def community_detail(request, pk):
    try:
        community = Community.objects.get(pk=pk)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = CommunitySerializer(community, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_community_by_id(request, pk):
    try:
        community = Community.objects.get(pk=pk)
        serializer = CommunitySerializer(community)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Community.DoesNotExist:
        return Response(
            {"error": "Komunitas tidak ditemukan."},
            status=status.HTTP_404_NOT_FOUND
        )
    
@api_view(['DELETE'])
def delete_image(request, pk):
    instance = get_object_or_404(Community, pk=pk)

    if instance.image:
        instance.image.delete(save=False)  
        instance.image = None  
        instance.save()  
        return Response({"message": "Gambar Anda berhasil dihapus"}, status=status.HTTP_204_NO_CONTENT)

    return Response({"error": "Tidak ada gambar yang ditemukan"}, status=status.HTTP_400_BAD_REQUEST)