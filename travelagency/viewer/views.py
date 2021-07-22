from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.views import View
from .models import Continent, Country, City, Hotel, Airport, Trip, TripPurchase, Blog
from .serializers import ContinentSerializer, CountrySerializer, HotelSerializer, CitySerializer, AirportSerializer, \
    TripPurchaseSerializer


# Create your views here.

def index(request):
    return render(request, "index.html")


def hot_tours(request):
    return render(request, "index-1.html")


def special_offers(request):
    countries = Country.objects.all()
    return render(request, "index-2.html", {'countries': countries})


def blog(request):
    blogs = Blog.objects.all()
    return render(request, "index-3.html", {'blogs': blogs})


def contacts(request):
    return render(request, "index-4.html")


@csrf_exempt
def continent_api(request):
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
    else:
        return JsonResponse("Failed to Delete", safe=False)


def counter_index(request):
    return render(request, "counter-index.html")


def counter(request):
    words = request.POST['text']
    no_of_words = len(words.split())
    return render(request, "counter.html", {'amount': no_of_words})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif username == "":
                messages.info(request, "Enter Username")
                return redirect('register')
            elif len(email) == 0:
                messages.info(request, "Enter Email")
                return redirect('register')
            elif password == "":
                messages.info(request, "Enter Password")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Login")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
