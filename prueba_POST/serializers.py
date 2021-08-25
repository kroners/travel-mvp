from rest_framework import serializers
from .models import prueba_POST

class prueba_POST_Serializer(serializers.ModelSerializer):
    class Meta:
        model= prueba_POST
        fields= '__all__'