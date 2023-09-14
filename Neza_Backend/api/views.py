from stagetracking.models import OrganizationStage
from stagetracking.models import OrganizationStageTracking
from .serializers import OrgStageSerializer
from .serializers import StageTrackingSerializer
from rest_framework.generics import ListAPIView
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics
from user_authentication.models import UserProfile
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
from rest_framework.views import APIView
from dashboard.models import Dashboard
from .serializers import DashboardSerializer


    
class OrganizationsInStageView(ListAPIView):
    serializer_class = OrgStageSerializer
    def get_queryset(self):
        stage_name = self.kwargs['stage_name']
        try:
           
            organizations_in_stage = OrganizationStage.objects.filter(
                Q(stage_name__iexact=stage_name)
            )
            return organizations_in_stage
        except OrganizationStage.DoesNotExist:
           
            error_message = f"No organizations found for stage '{stage_name}'."
            return JsonResponse({'error': error_message}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset, many=True).data
        result_data = []
        for item in data:
            organization_id = item['organization']
            organization = OrganizationStageTracking.objects.get(id=organization_id)
            item['organization_name'] = organization.organizationName
            result_data.append(item)

        return JsonResponse(result_data, safe=False, status=status.HTTP_200_OK)

    

class StageTrackingListView(APIView):
    def get(self, request):
        stagetracking =OrganizationStageTracking.objects.all() 
        serializer = StageTrackingSerializer(stagetracking, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StageTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Stage tracking created successfully",status=status.HTTP_201_CREATED)
        
        return Response("error while created stage tracking",status=status.HTTP_400_BAD_REQUEST)

class StageTrackingDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            stagetracking = OrganizationStageTracking.objects.get(id=id)
            serializer = StageTrackingSerializer(stagetracking)
            return Response(serializer.data)
        except OrganizationStageTracking.DoesNotExist:
            return Response("Stage tracking not found", status=status.HTTP_404_NOT_FOUND)
    
    
    def put(self,request,id,format=None):
         try:
            stagetracking = OrganizationStageTracking.objects.get(id=id)
            serializer = StageTrackingSerializer(stagetracking, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Stage tracking updated successfully", status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         except OrganizationStageTracking.DoesNotExist:
            return Response("Stage tracking not found", status=status.HTTP_404_NOT_FOUND)
       
    
    def delete(self,request,id,format=None):
        try:
            stagetracking = OrganizationStageTracking.objects.get(id=id)
            stagetracking.delete()
            return Response("Stage tracking successfully deleted", status=status.HTTP_204_NO_CONTENT)
        except OrganizationStageTracking.DoesNotExist:
            return Response("Stage tracking not found", status=status.HTTP_404_NOT_FOUND) 

        # users

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

# Create your views here.
class DashboardListView(APIView):
    def get(self,request):
        location_details = Dashboard.objects.all()
        serializer = DashboardSerializer(location_details, many=True)
        return Response(serializer.data)
    
