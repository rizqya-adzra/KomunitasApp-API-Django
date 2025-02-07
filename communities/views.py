from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Community
from roles.models import Role
from .serializers import CommunitySerializer

@api_view(['GET'])
def get_communities(request):
    communities = Community.objects.all()
    serializedData = CommunitySerializer(communities, many=True).data
    return Response(serializedData)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_joined_communities(request):
    user = request.user  

    joined_community = Role.objects.filter(user=user).values_list('community_id', flat=True)
    communities = Community.objects.filter(id__in=joined_community)

    serialized_data = CommunitySerializer(communities, many=True).data
    return Response(serialized_data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_communities(request):
    data = request.data
    serializer = CommunitySerializer(data=data)
    
    if serializer.is_valid():
        community = serializer.save()
        user = request.user

        role = Role.objects.create(user=user, community=community, role='ADMIN')

        if role:
            return Response({
                "message": "Komunitas berhasil dibuat.",
                "community": serializer.data,
                "role": {
                    "user": user.username,
                    "role": role.role
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "Komunitas dibuat, tetapi gagal menetapkan role ADMIN."
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    detailed_errors = {field: ", ".join(errors) for field, errors in serializer.errors.items()}
    
    return Response(
        {
            "message": "Data tidak valid.",
            "errors": detailed_errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def community_detail(request, pk):
    try:
        community = Community.objects.get(pk=pk)
    except Community.DoesNotExist:
        return Response({"message": "Komunitas tidak ditemukan."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        user_role = Role.objects.get(user=request.user, community=community)
        if user_role.role != 'ADMIN':
            return Response({"message": "Akses ditolak. Hanya ADMIN yang bisa mengedit atau menghapus komunitas."},
                            status=status.HTTP_403_FORBIDDEN)
    except Role.DoesNotExist:
        return Response({"message": "Anda bukan anggota komunitas ini."}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'DELETE':
        community.delete()
        return Response({"message": "Komunitas berhasil dihapus."}, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = CommunitySerializer(community, data=data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Komunitas berhasil diperbarui.", "community": serializer.data})
        
        return Response({"message": "Data tidak valid.", "errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def delete_image(request, pk):
    instance = get_object_or_404(Community, pk=pk)

    if instance.image:
        instance.image.delete(save=False)  
        instance.image = None  
        instance.save()  
        return Response({"message": "Gambar Anda berhasil dihapus"}, status=status.HTTP_204_NO_CONTENT)

    return Response({"error": "Tidak ada gambar yang ditemukan"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_community(request, pk):
    user = request.user
    try:
        community = Community.objects.get(pk=pk)
    except Community.DoesNotExist:
        return Response({"message": "Komunitas tidak ditemukan."}, status=status.HTTP_404_NOT_FOUND)
    
    if Role.objects.filter(user=user, community=community).exists():
        return Response({"message": "Anda sudah menjadi anggota komunitas ini."}, status=status.HTTP_400_BAD_REQUEST)
    
    if community.max_members and community.members.count() >= community.max_members:
        return Response({"message": "Komunitas sudah penuh."}, status=status.HTTP_400_BAD_REQUEST)

    Role.objects.create(user=user, community=community, role='MEMBER')
    return Response({"message": f"Selamat bergabung di Komunitas {community.name}!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_community_members(request, pk):
    role_filter = request.GET.get('role') 

    try:
        community = Community.objects.get(id=pk)
    except Community.DoesNotExist:
        return Response({"message": "Komunitas tidak ditemukan."}, status=status.HTTP_404_NOT_FOUND)
    
    if role_filter:
        roles = Role.objects.filter(community=community, role=role_filter.upper()).select_related('user')
    else:
        roles = Role.objects.filter(community=community).select_related('user')

    members_data = [
        {"id": role.user.id, "username": role.user.username, "role": role.role}
        for role in roles
    ]

    return Response({
        "community": community.name,
        "total_members": roles.count(),
        "members": members_data
    }, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def create_communities(request):
#     data = request.data
#     serializer = CommunitySerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     detailed_errors = {}
#     for field, errors in serializer.errors.items():
#         detailed_errors[field] = ", ".join(errors)
    
#     return Response(
#         {
#             "message": "Data tidak valid.",
#             "errors": detailed_errors
#         },
#         status=status.HTTP_400_BAD_REQUEST
#     )

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_communities(request):
#     data = request.data
#     serializer = CommunitySerializer(data=data)
    
#     if serializer.is_valid():
#         community = serializer.save()
#         user = request.user 

#         Role.objects.create(user=user, community=community, role='ADMIN')
        
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     detailed_errors = {field: ", ".join(errors) for field, errors in serializer.errors.items()}
    
#     return Response(
#         {
#             "message": "Data tidak valid.",
#             "errors": detailed_errors
#         },
#         status=status.HTTP_400_BAD_REQUEST
#     )

# @api_view(['PUT', 'DELETE'])
# def community_detail(request, pk):
#     try:
#         community = Community.objects.get(pk=pk)
#     except Community.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'DELETE':
#         community.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         data = request.data
#         serializer = CommunitySerializer(community, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)