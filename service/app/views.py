from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Location
from .serializers import LocationSerializer, CreateLocationSerializer


class LocationView(APIView):

    def get(self, request):
        ip = request.query_params.get('ip')
        if ip:
            location = get_object_or_404(Location.objects.all(), ip=ip)
            serializer = LocationSerializer(instance=location)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        if Location.objects.filter(ip=request.query_params.get('ip')).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        data = {"ip": (request.query_params.get('ip'))}
        serializer = CreateLocationSerializer(data=data)
        if serializer.is_valid():
            location_saved = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        ip = request.query_params.get('ip')
        if ip:
            location = get_object_or_404(Location.objects.all(), ip=ip)
            location.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
