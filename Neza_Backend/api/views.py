from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics
from user_registration.models import UserProfile
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserListView(APIView):
    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('Your account has been created successfully', status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, id, format=None):
        user = UserProfile.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        user = UserProfile.objects.get(id=id)
        serializer = UserSerializer(user, request.data)
        

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response('Server was unable to process your request. Please confirm that your credentials are valid', status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        user = UserProfile.objects.get(id=id)
        user.delete()
        
        return Response('User deleted successfully', status=status.HTTP_204_NO_CONTENT)
    
   
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = None
    if '@' in username:
        try:
            user = UserProfile.objects.get(email=username)
        except ObjectDoesNotExist:
            pass
    if not user:
        user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
