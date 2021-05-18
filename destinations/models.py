from django.db import models
from django.utils import timezone

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
    pais = models.ForeignKey(Country, related_name="pais", on_delete=models.DO_NOTHING)
    ciudad = models.ForeignKey(City, related_name="ciudad", on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, related_name="region", on_delete=models.DO_NOTHING, blank = True, null = True)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Destination, self).save(*args, **kwargs)