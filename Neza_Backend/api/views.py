import csv
import hashlib
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dataUpload.models import ExtractedData
from .serializers import ExtractedDataSerializer
import os

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        # Check if the uploaded file is a CSV
        if not uploaded_file.name.endswith('.csv'):
            return JsonResponse({'message': 'File contents are not needed in the database. Only CSV files are accepted.'}, status=400)

        file_content = uploaded_file.read().decode('utf-8')

        # Check if the uploaded file is a CSV
        if not uploaded_file.name.endswith('.csv'):
            return JsonResponse({'message': 'File contents are not needed in the database. Only CSV files are accepted.'}, status=400)

        # Rest of the code for processing the CSV file...
        try:
            reader = csv.DictReader(file_content.splitlines())
            header = next(reader)

            # Check if the header contains the expected columns
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

            # Calculate a hash of the file content
            file_hash = hashlib.md5(file_content.encode()).hexdigest()

            # Check if a record with the same hash already exists
            if ExtractedData.objects.filter(file_hash=file_hash).exists():
                return JsonResponse({'message': 'File contents already exist in the database'}, status=400)

            for row in reader:
                # Convert 'Yes' and 'No' to 1 and 0
                for column in ['sources of water', 'presence of open sewage']:
                    row[column] = 1 if row[column].lower() == 'yes' else 0

                # Save the file hash along with the data
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

            return JsonResponse({'message': 'File uploaded and processed successfully'})
        except csv.Error:
            return JsonResponse({'message': 'Invalid CSV file format'}, status=400)

    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)


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
