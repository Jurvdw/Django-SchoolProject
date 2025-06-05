from django.urls import path
from . import views

urlpatterns = [
                path("", views.load_indexpage, name = "index"),
                path("hello/", views.say_hello, name= "hello"),
                path("voornaam/", views.say_voornaam, name = "voornaam"),
                path("medal/<str:color>/", views.medalpage, name = "medal"),
                path("distances/", views.Distances, name= "Distances"),
                path('tijden/<str:length>/', views.times_by_length, name='times_by_length'),
               ]