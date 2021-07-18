from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.views import View
from .models import Continent, Country, City, Hotel, Airport, Trip, TripPurchase
from .serializers import ContinentSerializer, CountrySerializer, HotelSerializer, CitySerializer, AirportSerializer, \
    TripPurchaseSerializer


# Create your views here.

def index(request):
    return render(request, "index.html")


def hot_tours(request):
    return render(request, "index-1.html")


def special_offers(request):
    return render(request, "index-2.html")


def blog(request):
    return render(request, "index-3.html")


def contacts(request):
    return render(request, "index-4.html")


def counter_index(request):
    return render(request, "counter-index.html")


def counter(request):
    words = request.POST['text']
    no_of_words = len(words.split())
    return render(request, "counter.html", {'amount': no_of_words})


@csrf_exempt
def continent_api(request, id=0):
    if request.method == 'GET':
        continents = Continent.objects.all()
        continents_serializer = ContinentSerializer(continents, many=True)
        return JsonResponse(continents_serializer.data, safe=False)

    elif request.method == 'POST':
        continent_data = JSONParser().parse(request)
        continent_serializer = ContinentSerializer(data=continent_data)
        if continent_serializer.is_valid():
            continent_serializer.save()
            return JsonResponse('Added Successfully!!', safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        continent_data = JSONParser().parse(request)
        continent = Continent.objects.get(continent_id=continent_data['continent_id'])
        continent_serializer = ContinentSerializer(continent, data=continent_data)
        if continent_serializer.is_valid():
            continent_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        continent = Continent.objects.get(continent_id=id)
        continent.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    return JsonResponse("Failed to Delete", safe=False)
