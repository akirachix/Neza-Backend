from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics
from user_registration.models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout


class UserView(generics.ListCreateAPIView):
    users = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data = request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            org_type = serializer.validated_data['org_type']
            website = serializer.validated_data['website']
            phone_number = serializer.validated_data['phone_number']

            user = UserProfile.objects.create_user(username=username, email=email, password=password, org_type=org_type, website=website, phone_number=phone_number)

            return Response('Your account has been created successfully', status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    users = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


    def put(self, request):
        
        user = request.user
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response('Server was unable to process your request, please check if your credentials are valid', status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        user = request.user
        if user:
            user.delete()

            return Response('User deleted successfully', status = status.HTTP_204_NO_CONTENT)
        
        return Response('You do not have permission to delete this user', status = status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = None

    user = authenticate(username=username, password=password)

    if user is None and '@' in username:
        try:
            user_profile = UserProfile.objects.get(email=username)
            user = user_profile

        except UserProfile.DoesNotExist:
            pass

    if user:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
