from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date, datetime
# from __future__ import unicode_literals
import calendar


# Create your models here.
class Continent(models.Model):
    name = models.CharField('Continent Name', max_length=15)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField('Country Name', max_length=60)
    continent = models.ForeignKey(Continent, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField('City Name', max_length=90)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField('Hotel Name', max_length=150)
    hotel_standard = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])
    hotel_description = models.TextField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField('Airport Name', max_length=350, default="")
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField('Trip Name', max_length=350)
    departure = models.ForeignKey(Airport, related_name='flight_departure', on_delete=models.DO_NOTHING, null=True,
                                  blank=True)
    arrival = models.ForeignKey(Airport, related_name='flight_arrival', on_delete=models.DO_NOTHING, null=True,
                                blank=True)
    # Trip.arrival_city.country = country of city
    arrival_city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)
    hotel_booked = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_of_departure = models.DateTimeField('Flight Departure Date')
    date_of_arrival = models.DateTimeField('Flight Arrival Date')
    date_of_return = models.DateTimeField('Customer Return Date')
    number_of_days_stay = models.PositiveIntegerField('Length of Stay')
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
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField('Contact Phone', max_length=25)
    email_address = models.EmailField('User Email Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class TripPurchase(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING, null=True, blank=True)
    trip_description = models.TextField(null=True, blank=True)
    travellers = models.ManyToManyField(Customer, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.trip.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000, null=True, blank=True)
    created_at = models.DateField(default=datetime.now(), null=True, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title
