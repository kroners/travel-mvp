from rest_framework import serializers

from .models import (
    City,
    Region,
    Country,
    Destination
)

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id',
            'nombre',
            'pais',
            'ciudad',
            'region'
        ]

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id',
            'codigoPais',
            'nombre'
        ]
