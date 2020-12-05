from django.db import models
from destinations.models import Destination

# Create your models here.
class HotelCategory(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class Service(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class ServiceType(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class RoomType(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    hotel = models.ForeignKey(HotelCategory, on_delete=models.DO_NOTHING)

class FoodService(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class TripProfile(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class Activity(models.Model):
    descripcion = models.CharField(max_length=500)
    destinos = models.ManyToManyField(Destination, related_name='destinos', blank=True)

class TravelerType(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class Language(models.Model):
    nombre = models.CharField(max_length=50)
