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

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id',
            'codigoRegion',
            'nombre'
        ]

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields=('id',
            'nombre',
            'pais',
            'ciudad',
            'region'
        )
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        self.fields['pais'] = CountrySerializer(many=False, read_only=True)
        self.fields['ciudad'] = CitySerializer(many=False, read_only=True)
        self.fields['region'] = RegionSerializer(many=False, read_only=True)
        return super(DestinationSerializer, self).to_representation(instance)
