
import csv
from rest_framework.views import APIView
from dataUpload.models import DataUpload
from .serializers import DataUploadSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from dataUpload.models import ExtractedData  

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
                'location',
                'sources of water',
                'proximity to industries',
                'number of garages in an area',
                'proximity to dumpsite',
                'presence of open sewage',
                'Past cases of lead poisoning',
                'population (women and children)',
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
