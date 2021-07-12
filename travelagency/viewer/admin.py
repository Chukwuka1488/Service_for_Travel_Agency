from django.contrib import admin
from .models import Continent, Country, City, Hotel, Airport, Trip, TripPurchase

# Register your models here.
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Airport)
admin.site.register(Trip)
admin.site.register(TripPurchase)
