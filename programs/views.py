from django.http import HttpResponse, JsonResponse, Http404
from django.db.models import Q
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Program
from .serializers import ProgramSerializer

# Create your views here.
class ProgramList(generics.ListAPIView):
    serializer_class = ProgramSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        # An example of all the queryset would be programs/?destinos=1,10&duracion=5&precio_min=100&precio_max=1000&
        # adultos=1&ninos=1&bebes=1&servicios=2,3&tipo_servicio=2&tipo_hospedaje=3&tipo_habitacion=2&alimentacion=3&
        # actividades=2,4,5,7,8&perfil_viaje=3&idioma=1
        programs = Program.objects.all()
        # keywords = []

        destinos = self.request.query_params.getlist('destinos', None)
        duracion = self.request.query_params.get('duracion', None)
        precio_min = self.request.query_params.get('precio_min', 0)
        precio_max = self.request.query_params.get('precio_max', None)
        adultos = self.request.query_params.get('adultos', None)
        ninos = self.request.query_params.get('ninos', None)
        bebes = self.request.query_params.get('bebes', None)
        servicios = self.request.query_params.get('servicios', None)
        tipo_servicio = self.request.query_params.get('tipo_servicio', None)
        tipo_hospedaje = self.request.query_params.get('tipo_hospedaje', None)
        tipo_habitacion = self.request.query_params.get('tipo_habitacion', None)
        alimentacion = self.request.query_params.get('alimentacion', None)
        actividades = self.request.query_params.get('actividades', None)
        perfil_viaje = self.request.query_params.get('perfil_viaje', None)
        idioma = self.request.query_params.get('idioma', None)

        if destinos is not None:
            programs = programs.filter(destinos__id__in=destinos)
        
        if duracion is not None:
            programs = programs.filter(duracion=duracion)
        
        if precio_max is not None:
            programs = programs.filter(precio__range=(precio_min, precio_max))
        
        if adultos is not None:
            programs = programs.filter(personas__tipoPersona__id=1).filter(personas__cantidad=adultos)
        if ninos is not None:
            programs = programs.filter(personas__tipoPersona__id=2).filter(personas__cantidad=ninos)
        if bebes is not None:
            programs = programs.filter(personas__tipoPersona__id=3).filter(personas__cantidad=bebes)
        
        if servicios is not None:
            programs = programs.filter()
        
        if tipo_servicio is not None:
            programs = programs.filter()

        return programs
        # serializer = ProgramSerializer(programs, many=True)
        # print(serializer)
        # return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgramDetail(APIView):
    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        program = self.get_object(pk)
        serializer = ProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        program = self.get_object(pk)
        program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
