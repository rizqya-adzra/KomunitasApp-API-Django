from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Chat
from .serializers import ChatSerializer

@api_view(['GET'])
def get_chats(request):
    chats = Chat.objects.all()
    serializedData = ChatSerializer(chats, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def get_chat_by_id(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    serializer = ChatSerializer(chat)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_chat(request):
    data = request.data
    serializer = ChatSerializer(data=data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_chat(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    serializer = ChatSerializer(chat, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_chat(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    chat.delete()
    return Response({'message': 'Chat Berhasil di hapus'}, status=status.HTTP_204_NO_CONTENT)
