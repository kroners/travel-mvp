from django.db import models

# Create your models here.
class City(models.Model):
    codigoCiudad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)

class Region(models.Model):
    codigoRegion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)

class Country(models.Model):
    codigoPais = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)

class Destination(models.Model):
    nombre = models.CharField(max_length=20)
    pais = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    ciudad = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)