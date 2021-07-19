from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Continent(models.Model):
    continent_id = models.AutoField(primary_key=True)
    continent_name = models.CharField(max_length=15)

    def __str__(self):
        return self.continent_name


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=60)
    continent = models.ForeignKey(Continent, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=90)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.city_name


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=150)
    hotel_standard = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])
    hotel_description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.hotel_name


class Airport(models.Model):
    airport_id = models.AutoField(primary_key=True)
    airport_name = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.airport_name


class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    departure = models.ForeignKey(Airport, related_name='flight_departure', on_delete=models.DO_NOTHING, null=True, blank=True)
    arrival = models.ForeignKey(Airport, related_name='flight_arrival', on_delete=models.DO_NOTHING, null=True, blank=True)
    arrival_city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)
    hotel_booked = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_of_departure = models.DateTimeField()
    date_of_arrival = models.DateTimeField()
    date_of_return = models.DateTimeField()
    number_of_days_stay = models.PositiveIntegerField()
    trip_choice = (
        ('Bed & Breakfast', 'BB'),
        ('HalfBoard', 'HB'),
        ('FullBoard', 'FB'),
        ('All Inclusive', 'AI'),
    )
    type_of_trip = models.CharField(max_length=30, blank=True, null=True, choices=trip_choice)
    adult_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    children_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    promoted = models.BooleanField()
    total_adult_places = models.PositiveIntegerField()
    total_children_places = models.PositiveIntegerField()
    available_adult_places = models.PositiveIntegerField()
    available_children_places = models.PositiveIntegerField()

    def __str__(self):
        return f"Your trip with ID No {self.trip_id} departs {self.departure} at {self.date_of_departure} " \
               f"and arrives {self.arrival} in {self.arrival_city} at {self.date_of_arrival}. You will be " \
               f"lodged at {self.hotel_booked} for {self.number_of_days_stay} and your flight return is " \
               f"scheduled for {self.date_of_return}"


class TripPurchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    trip_id = models.ForeignKey(Trip, on_delete=models.DO_NOTHING, null=True, blank=True)
    trip_description = models.TextField()
    user = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.trip_description
