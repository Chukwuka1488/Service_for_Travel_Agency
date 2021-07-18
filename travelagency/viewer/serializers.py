from rest_framework import serializers
from viewer.models import Continent, Country, City, Hotel, Airport, Trip, TripPurchase


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ('continent_id',
                  'continent')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_id',
                  'country',
                  'continent')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city_id',
                  'city',
                  'country')


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_id',
                  'hotel_name',
                  'hotel_standard', 'hotel_description', 'city')


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('airport_id',
                  'airport_name',
                  'city')


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('trip_id',
                  'departure',
                  'arrival',
                  'arrival_city',
                  'hotel_booked',
                  'date_of_departure',
                  'date_of_arrival',
                  'date_of_return',
                  'number_of_days_stay',
                  'type_of_trip',
                  'adult_price',
                  'children_price',
                  'promoted',
                  'total_adult_places',
                  'total_children_places',
                  'available_adult_places',
                  'available_children_places'
                  )


class TripPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPurchase
        fields = ('purchase_id ',
                  'trip_id',
                  'trip_description',
                  'user ',
                  'total_cost'
                  )
