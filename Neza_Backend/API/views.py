from django.shortcuts import render
from User_Registration.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, request.data)
        

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response('User deleted successfully', status=status.HTTP_204_NO_CONTENT)
