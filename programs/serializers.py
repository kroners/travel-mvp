from rest_framework import serializers

from .models import (
    Program,
    Itinerary,
    Include,
    NoInclude,
    ProgramQuantity,
    ProgramActivity,
    ProgramCost
    
)
from destinations.models import Destination

class ProgramSerializer(serializers.ModelSerializer):
    idioma = serializers.StringRelatedField(many=False)
    precios = serializers.StringRelatedField(many=True)
    incluidos = serializers.StringRelatedField(many=True)
    no_incluidos = serializers.StringRelatedField(many=True)
    itinerario = serializers.StringRelatedField(many=True)
    personas = serializers.StringRelatedField(many=True)
    actividades = serializers.StringRelatedField(many=True)
    destinos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Program
        fields = ['id', 
            'titulo', 
            'descripcion', 
            'duracion', 
            'fechaInicio', 
            'fechaFin', 
            'idioma',
            'precios',
            'incluidos',
            'no_incluidos',
            'itinerario',
            'personas',
            'actividades',
            'destinos'
        ]

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ['id', 
            'titulo', 
            'descripcion', 
            'duracion', 
            'fechaInicio', 
            'fechaFin', 
            'idioma'
            ]

class IncludeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Include
        fields = ['id', 
            'descripcion',
            ]

class NoIncludeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoInclude
        fields = ['id', 
            'descripcion',
            ]

class ProgramQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramQuantity
        fields = ['id', 
            'cantidad',
            'tipoPersona'
            ]
        
class ProgramActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramActivity
        fields = ['id', 
            'actividad',
            ]
        
class ProgramCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramCost
        fields = ['id', 
            'precio',
            'habitacion'
            ]


