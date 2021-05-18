from rest_framework import serializers

from .models import (
    City,
    Region,
    Country,
    Destination
)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id',
            'codigoPais',
            'nombre'
        ]

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id',
            'codigoCiudad',
            'nombre'
        ]

class DestinationSerializer(serializers.ModelSerializer):
    pais = CountrySerializer(many=False, read_only=True)
    ciudad = CitySerializer(many=False, read_only=True)

    class Meta:
        model = Destination
        fields = ['id',
            'nombre',
            'pais',
            'ciudad',
            'region'
        ]
