from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class prueba_POST(models.Model):
    adultos = models.IntegerField(default=0)
    bebes = models.IntegerField(default=0)
    conGuia = models.BooleanField(default=False)
    confort = models.BooleanField(default=False)
    destinationFromSearch = ArrayField(models.CharField(max_length=200))
    doble = models.BooleanField(default=False)
    duracion = models.IntegerField(default=0)
    estandar = models.BooleanField(default=False)
    excursiones = models.BooleanField(default=False)
    lujo = models.BooleanField(default=False)
    mediaPension = models.BooleanField(default=False)
    niños = models.IntegerField(default=0)
    pensionCompleta= models.BooleanField(default=False)
    presupuesto= ArrayField(models.IntegerField())
    regular= models.BooleanField(default=False)
    selectedDateEnd= models.DateTimeField()
    selectedDateStart= models.DateTimeField()
    shows= models.BooleanField(default=False)
    sinGuia= models.BooleanField(default=False)
    single= models.BooleanField(default=False)
    soloDesayuno= models.BooleanField(default=False)
    traslados= models.BooleanField(default=False)
    triple= models.BooleanField(default=False)
    










