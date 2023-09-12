from django.http import JsonResponse
import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from dataUpload.models import DataUpload
from .serializers import DataUploadSerializer
from dataUpload.models import ExtractedData
from rest_framework.decorators import api_view


class DataUploadListView(APIView):
    def get(self, request):
        try:
            dataUploads = DataUpload.objects.all()
            serializer = DataUploadSerializer(dataUploads, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = DataUploadSerializer(data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                response = self.extract_and_process_data(instance)

                url = reverse('data_upload_detail_view', args=[instance.pk], request=request)

                return Response(serializer.data, status=status.HTTP_201_CREATED, headers={'Location': url})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def extract_and_process_data(self, data_upload_instance):
        try:
            csv_file = data_upload_instance.file.path

            columns_to_extract = [
                "location",
                "sources of water",
                "proximity to industries",
                "number_of_garages_in_area",
                "proximity_to_dumpsite",
                "presence_of_open_sewage",
                "past_cases_of_lead_poisoning",
                "women_and_children_population",
            ]

            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    extracted_row = {}
                    for column in columns_to_extract:
                        extracted_row[column] = row.get(column)

                    extracted_instance = ExtractedData(**extracted_row)
                    extracted_instance.save()

            return Response("Data extracted and saved successfully", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"An error occurred while extracting and saving data: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DataUploadDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            dataUpload = DataUpload.objects.get(id=id)
            serializer = DataUploadSerializer(dataUpload)
            return Response(serializer.data)
        except DataUpload.DoesNotExist:
            return Response("DataUpload not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id, format=None):
        try:
            dataUpload = DataUpload.objects.get(id=id)
            serializer = DataUploadSerializer(dataUpload, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DataUpload.DoesNotExist:
            return Response("DataUpload not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id, format=None):
        try:
            dataUpload = DataUpload.objects.get(id=id)
            dataUpload.delete()
            return Response("File successfully deleted", status=status.HTTP_204_NO_CONTENT)
        except DataUpload.DoesNotExist:
            return Response("DataUpload not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_content = uploaded_file.read().decode('utf-8')

        expected_columns = ["location", "proximity to industries", "women_and_children_population", "past_cases_of_lead_poisoning"]

        try:
            reader = csv.DictReader(file_content.splitlines())
            header = next(reader)

            for column in expected_columns:
                if column not in header:
                    return JsonResponse({'message': f'Missing column: {column}'}, status=400)

            for row in reader:
                extracted_data = ExtractedData(
                    location=row["location"],
                    sources_of_water=row["sources of water"],
                    proximity_to_industries=row["proximity to industries"],
                    number_of_garages_in_area=row["number_of_garages_in_area"],
                    proximity_to_dumpsite=row["proximity_to_dumpsite"],
                    presence_of_open_sewage=row["presence_of_open_sewage"],
                    past_cases_of_lead_poisoning=row["past_cases_of_lead_poisoning"],
                    women_and_children_population=row["women_and_children_population"],
                )
                extracted_data.save()

            return JsonResponse({'message': 'File uploaded and processed successfully'})
        except csv.Error:
            return JsonResponse({'message': 'Invalid CSV file format'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from dataUpload.models import ExtractedData
from .serializers import ExtractedDataSerializer  

class ExtractedDataListView(APIView):
    def get(self, request):
        extracted_data = ExtractedData.objects.all()

        serializer = ExtractedDataSerializer(extracted_data, many=True)

        return Response(serializer.data)



class ExtractedDataDeleteView(APIView):
    def delete(self, request, pk):
        try:
            extracted_data = ExtractedData.objects.get(pk=pk)
            extracted_data.delete()
            return Response("File successfully deleted",status=status.HTTP_204_NO_CONTENT)
        except ExtractedData.DoesNotExist:
            return Response("ExtractedData not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ExtractedDataUpdateFileView(APIView):
    def put(self, request, pk):
        try:
            extracted_data = ExtractedData.objects.get(pk=pk)
            extracted_data.file = request.FILES.get('new_file')
            extracted_data.save()

            serializer = ExtractedDataSerializer(extracted_data)

            return Response(serializer.data)
        except ExtractedData.DoesNotExist:
            return Response("ExtractedData not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



