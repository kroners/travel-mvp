from rest_framework import serializers

from .models import HotelCategory
from .models import Service, ServiceType
from .models import RoomType
from .models import FoodService
from .models import TripProfile
from .models import Activity
from .models import TravelerType
from .models import Language

class HotelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelCategory
        fields = ['id', 'nombre', 'descripcion']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'nombre', 'descripcion']

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'nombre', 'descripcion']

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'nombre', 'descripcion', 'hotel']

class FoodServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodService
        fields = ['id', 'nombre', 'descripcion']

class TripProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripProfile
        fields = ['id', 'nombre', 'descripcion']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'nombre', 'descripcion']

class TravelerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelerType
        fields = ['id', 'nombre', 'descripcion']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'nombre']
