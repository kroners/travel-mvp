from django.contrib import admin
from destinations.models import Destination
from destinations.models import City
from destinations.models import Region
from destinations.models import Country
# Register your models here.
admin.site.register(Destination)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Country)


