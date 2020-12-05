from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    HotelCategory,
    Service,
    ServiceType,
    RoomType,
    FoodService,
    TripProfile,
    Activity,
    TravelerType,
    Language
)
from .serializers import (
    HotelCategorySerializer, 
    ServiceSerializer, 
    ServiceTypeSerializer,
    RoomTypeSerializer,
    FoodServiceSerializer,
    TripProfileSerializer,
    ActivitySerializer,
    TravelerTypeSerializer,
    LanguageSerializer
)

# Create your views here.
class HotelCategoryList(APIView):
    def get(self, request, format=None):
        hotel_categories = HotelCategory.objects.all()
        serializer = HotelCategorySerializer(hotel_categories, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = HotelCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelCategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return HotelCategory.objects.get(pk=pk)
        except HotelCategory.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        hotel_category = self.get_object(pk)
        serializer = HotelCategorySerializer(hotel_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        hotel_category = self.get_object(pk)
        hotel_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ServiceList(APIView):
    def get(self, request, format=None):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceDetail(APIView):
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        services = self.get_object(pk)
        serializer = ServiceSerializer(services, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        service = self.get_object(pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ServiceTypeList(APIView):
    def get(self, request, format=None):
        service_types = ServiceType.objects.all()
        serializer = ServiceTypeSerializer(service_types, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ServiceTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceTypeDetail(APIView):
    def get_object(self, pk):
        try:
            return ServiceType.objects.get(pk=pk)
        except ServiceType.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        service_types = self.get_object(pk)
        serializer = ServiceTypeSerializer(service_types, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        servive_type = self.get_object(pk)
        servive_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class RoomTypeList(APIView):
    def get(self, request, format=None):
        room_types = RoomType.objects.all()
        serializer = RoomTypeSerializer(room_types, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomTypeDetail(APIView):
    def get_object(self, pk):
        try:
            return RoomType.objects.get(pk=pk)
        except RoomType.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        room_type = self.get_object(pk)
        serializer = RoomTypeSerializer(room_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        room_type = self.get_object(pk)
        room_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class FoodServiceList(APIView):
    def get(self, request, format=None):
        food_services = FoodService.objects.all()
        serializer = FoodServiceSerializer(food_services, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = FoodServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodServiceDetail(APIView):
    def get_object(self, pk):
        try:
            return FoodService.objects.get(pk=pk)
        except FoodService.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        food_service = self.get_object(pk)
        serializer = FoodServiceSerializer(food_service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        food_service = self.get_object(pk)
        food_service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class TripProfileList(APIView):
    def get(self, request, format=None):
        trip_profiles = TripProfile.objects.all()
        serializer = TripProfileSerializer(trip_profiles, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = TripProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TripProfileDetail(APIView):
    def get_object(self, pk):
        try:
            return TripProfile.objects.get(pk=pk)
        except TripProfile.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        trip_profile = self.get_object(pk)
        serializer = TripProfileSerializer(trip_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        trip_profile = self.get_object(pk)
        trip_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ActivityList(APIView):
    def get(self, request, format=None):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityDetail(APIView):
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class TravelerTypeList(APIView):
    def get(self, request, format=None):
        traveler_types = TravelerType.objects.all()
        serializer = TravelerTypeSerializer(traveler_types, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = TravelerTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TravelerTypeDetail(APIView):
    def get_object(self, pk):
        try:
            return TravelerType.objects.get(pk=pk)
        except TravelerType.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        traveler_type = self.get_object(pk)
        serializer = TravelerTypeSerializer(traveler_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        traveler_type = self.get_object(pk)
        traveler_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class LanguageList(APIView):
    def get(self, request, format=None):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LanguageDetail(APIView):
    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        language = self.get_object(pk)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)