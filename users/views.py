from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from .models import User

# from django.contrib.auth import get_user_model
from .serializers import UserSerializer
  
# @api_view(['POST'])
# def user_login(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     if email and '@' in email:
#         try:
#             user = User.objects.get(email=email)
#             if user and check_password(password, user.password):
#                 token, _ = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_200_OK)
#             return Response({'error': 'Email atau Password Anda salah.'}, status=status.HTTP_401_UNAUTHORIZED)
#         except User.DoesNotExist:
#             return Response({'error': 'Email atau Password Anda salah.'}, status=status.HTTP_401_UNAUTHORIZED)
#     return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email and '@' in email:
        try:
            user = User.objects.get(email=email)
            if user and check_password(password, user.password):
                user.is_active = True
                user.last_login = now()
                user.save()
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Email atau Password Anda salah.'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'Email atau Password Anda salah.'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_user(request):
    data = request.data
    data['password'] = make_password(data['password'])  
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user) 
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_logout(request):
#     try:
#         request.user.auth_token.delete() 
#         return Response({'message': 'Anda berhasil logout!'}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    try:
        request.user.auth_token.delete()

        user = request.user
        user.is_active = False  
        user.last_login = now() 
        user.save()

        return Response({'message': 'Anda berhasil logout!'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_users(request):
    users = User.objects.all()
    serializedData = UserSerializer(users, many=True).data
    return Response(serializedData)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated]) 
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data.copy()
        if 'password' in data:
            data['password'] = make_password(data['password'])

        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET'])
# def get_user_by_id(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     serializer = UserSerializer(user)
#     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_by_id(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def custom_auth_token(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     if not email or not password:
#         return Response({'error': 'Email and password are required'}, status=400)

#     try:
#         User = get_user_model()
#         user = User.objects.get(email=email)

#         if not check_password(password, user.password):
#             return Response({'non_field_errors': ['Unable to log in with provided credentials.']}, status=400)

#         token, created = Token.objects.get_or_create(user=user)

#         return Response({
#             'token': token.key,
#             'user_id': user.id,
#             'email': user.email,
#             'name': user.username,
#         })
#     except User.DoesNotExist:
#         return Response({'non_field_errors': ['Unable to log in with provided credentials.']}, status=400)


