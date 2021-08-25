from django.db import models
from services.models import Language, TravelerType, Activity, RoomType, Service, ServiceType, FoodService, TripProfile
from destinations.models import Destination

# Create your models here.
class Program(models.Model):
    titulo = models.CharField(max_length=400)
    descripcion = models.CharField(max_length=1000)
    duracion = models.IntegerField()
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    idioma = models.OneToOneField(Language, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Itinerary(models.Model):
    dia = models.IntegerField()
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    programa = models.ForeignKey(Program, related_name="itinerario", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Include(models.Model):
    descripcion = models.CharField(max_length=1000)
    programa = models.ForeignKey(Program, related_name="incluidos", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class NoInclude(models.Model):
    descripcion = models.CharField(max_length=1000)
    programa = models.ForeignKey(Program, related_name="no_incluidos", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ProgramQuantity(models.Model):
    cantidad = models.IntegerField()
    tipoPersona = models.ForeignKey(TravelerType, on_delete=models.CASCADE)
    programa = models.ForeignKey(Program, related_name="personas", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ProgramActivity(models.Model):
    actividad = models.ForeignKey(Activity, on_delete=models.CASCADE)
    programa = models.ForeignKey(Program, related_name="actividades", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ProgramCost(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    habitacion = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    programa = models.ForeignKey(Program, related_name="precios", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ProgramDestination(models.Model):
    destino = models.ForeignKey(Destination, on_delete=models.CASCADE)
    programa = models.ForeignKey(Program, related_name="destinos", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ProgramServices(models.Model):
    servicio = models.ForeignKey(Service, on_delete=models.CASCADE)
    programa = models.ForeignKey(Program, related_name="servicios", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ProgramDetails(models.Model):
    tipo_servicio = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    alimentacion = models.ForeignKey(FoodService, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    perfil_viaje = models.ForeignKey(TripProfile, on_delete=models.CASCADE)
    programa = models.ForeignKey(Program, related_name="detalles_servicio", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



