from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tours', views.hot_tours, name='hot_tours'),
    path('blog', views.blog, name='blog'),
    path('contacts', views.contacts, name='contact'),
    path('offers', views.special_offers, name='special_offers'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('hotels', views.hotels, name='hotels'),

    path('continents', views.continent_api, name='continents'),

    path('counterIndex', views.counter_index, name='counter_form'),
    path('counter', views.counter, name='counter'),

]
