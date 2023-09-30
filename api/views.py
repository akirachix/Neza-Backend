import csv
import hashlib
from rest_framework.parsers import FileUploadParser
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dataUpload.models import ExtractedData
from .serializers import ExtractedDataSerializer
import os
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
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
import joblib
import json
from django.views.decorators.csrf import csrf_exempt




# account views

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
        
        return Response("error while creating stage tracking",status=status.HTTP_400_BAD_REQUEST)

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
    queryset = UserProfile.objects.all()
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
    queryset= UserProfile.objects.all()
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
            image = request.data.get('image')
            if image:
                user.account.image = image
                user.account.save()

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
# profile 

class ProfileImageView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request):
        user = request.user
        image = request.data['image']

        if image:
            user.account.image = image
            user.account.save()

            return Response({'message': 'Profile image updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Image data is missing'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        if not uploaded_file.name.endswith('.csv'):
            return JsonResponse({'message': 'File contents are not needed in the database. Only CSV files are accepted.'}, status=400)

        file_content = uploaded_file.read().decode('utf-8')

        try:
            reader = csv.DictReader(file_content.splitlines())
            header = next(reader)

            expected_columns = [
                "location",
                "sources of water",
                "proximity to industries",
                "number of garages in an area",
                "proximity to dumpsite",
                "presence of open sewage",
                "past cases of lead poisoning",
                "women and children population",
            ]

            for column in expected_columns:
                if column not in header:
                    return JsonResponse({'message': f'Missing column: {column}'}, status=400)

            file_hash = hashlib.md5(file_content.encode()).hexdigest()

            if ExtractedData.objects.filter(file_hash=file_hash).exists():
                return JsonResponse({'message': 'File contents already exist in the database'}, status=400)

            for row in reader:
                row["sources of water"] = 1 if row["sources of water"].lower() == 'yes' else 0
                row["presence of open sewage"] = 1 if row["presence of open sewage"].lower() == 'yes' else 0

                extracted_data = ExtractedData(
                    location=row["location"],
                    sources_of_water=row["sources of water"],
                    proximity_to_industries=row["proximity to industries"],
                    number_of_garages_in_area=row["number of garages in an area"],
                    proximity_to_dumpsite=row["proximity to dumpsite"],
                    presence_of_open_sewage=row["presence of open sewage"],
                    past_cases_of_lead_poisoning=row["past cases of lead poisoning"],
                    women_and_children_population=row["women and children population"],
                    file_hash=file_hash,
                )
                extracted_data.save()
                print(".............................>>>>>>>>>>>>>>>>>>>>>")
            return JsonResponse({'message': 'File uploaded and processed successfully'})
        except csv.Error:
            return JsonResponse({'message': 'Invalid CSV file format'}, status=400)

    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)

class DashboardListView(APIView):
    def get(self,request):
        location_details = Dashboard.objects.all()
        serializer = DashboardSerializer(location_details, many=True)
        return Response(serializer.data)

class ExtractedDataListView(APIView):
    def get(self, request):
        try:
            extracted_data = ExtractedData.objects.all()
            serializer = ExtractedDataSerializer(extracted_data, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ExtractedDataDetailView(APIView):
    def get(self, request, pk):
        try:
            extracted_data = ExtractedData.objects.get(pk=pk)
            serializer = ExtractedDataSerializer(extracted_data)
            return Response(serializer.data)
        except ExtractedData.DoesNotExist:
            return Response("ExtractedData not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class ExtractedDataDeleteView(APIView):
    def delete(self, request, pk):
        try:
            extracted_data = ExtractedData.objects.get(pk=pk)
            extracted_data.delete()
            return Response("ExtractedData successfully deleted", status=status.HTTP_204_NO_CONTENT)
        except ExtractedData.DoesNotExist:
            return Response("ExtractedData not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


nb_model = joblib.load('/Neza-Backend/neza_model.pkl')

@csrf_exempt
def predict(request):
    if request.method == 'GET':
        try:
            precomputed_predictions = nb_model.predict()
            predictions_list = precomputed_predictions.tolist()

            return JsonResponse ({'predictions': predictions_list})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)