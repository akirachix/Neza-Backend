
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from dataUpload.models import ExtractedData
from .serializers import ExtractedDataSerializer
from django.http import Http404

class ExtractedDataDetailView(APIView):
    def get_object(self, pk):
        try:
            return ExtractedData.objects.get(pk=pk)
        except ExtractedData.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        extracted_data = self.get_object(pk)
        serializer = ExtractedDataSerializer(extracted_data)
        return Response(serializer.data)

    def delete(self, request, pk):
        extracted_data = self.get_object(pk)
        extracted_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
