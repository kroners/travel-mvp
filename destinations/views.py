from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Destination, Country, City
from .serializers import DestinationSerializer, CountrySerializer, CitySerializer

# Create your views here.
class DestinationList(APIView):
    serializer_class = DestinationSerializer
    model = serializer_class.Meta.model

    # Define query search and apply filter
    def get_queryset(self):
        # Define search word for query
        destino = self.request.query_params.get('destino', None)
        print(destino)
        destinations = Destination.objects.all()

        if destino is not None:
            destinations = destinations.filter(nombre__icontains=destino)
        return destinations
    
    # Get list of destinations by query search
    def get(self, request):
        destinations = self.get_queryset()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

    # Create a new destination
    def post(self, request, format=None):
        print(request.data)
        serializer = DestinationSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DestinationDetail(APIView):
    def get_object(self, pk):
        try:
            return Destination.objects.get(pk=pk)
        except Destination.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        destination = self.get_object(pk)
        serializer = DestinationSerializer(destination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        destination = self.get_object(pk)
        destination.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
class CountryList(APIView):
    serializer_class = CountrySerializer
    model = serializer_class.Meta.model
    def get(self, request, format=None):
        paises = Country.objects.all()
        serializer = CountrySerializer(paises, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityList(APIView):
    serializer_class = CitySerializer
    model = serializer_class.Meta.model
    def get(self, request, format=None):
        paises = City.objects.all()
        serializer = CitySerializer(paises, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print(request.data)
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
