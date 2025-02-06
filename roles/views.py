from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Role
from .serializers import RoleSerializer

# @api_view(['GET'])
# def get_roles(request):
#     roles = Role.objects.all()
#     serializedData = RoleSerializer(roles, many=True).data
#     return Response(serializedData)

@api_view(['GET'])
def get_roles(request):
    # community = request.query_params.get('community')  
    # if not community:
    #     return Response({"error": "community_id nya tidak masuk"}, status=status.HTTP_400_BAD_REQUEST)
    roles = Role.objects.all() 
    serializerData = RoleSerializer(roles, many=True).data
    return Response(serializerData, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_roles(request):
    user = request.data.get('user')

    if Role.objects.filter(user=user).exists():
        return Response({"error": "User sudah mempunyai role"}, status=status.HTTP_400_BAD_REQUEST)

    data = request.data
    serializer = RoleSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)