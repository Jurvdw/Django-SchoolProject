from django.shortcuts import render
from django.http import  HttpResponse
from .models import Distance, Time
from django.shortcuts import render, get_object_or_404

def say_hello(request):
    return render(request, "base/hello.html")

def say_voornaam(request):
    context = {"first_name": "Jur", "last_name": "Welle", "age": 19}
    return render(request, "base/voornaam.html", context)

def medalpage(request, color):
    context = {
  "langlaufen_medal_winners": {
    "Gold": {
      "Name": "Dario Cologna",
      "Country": "Switzerland",
      "Time": "33:43.9"
    },
    "Silver": {
      "Name": "Simen Hegstad Krüger",
      "Country": "Norway",
      "Time": "34:02.2"
    },
    "Bronze": {
      "Name": "Denis Spitsov",
      "Country": "Russia",
      "Time": "34:06.9"
    }
  }
}
    
    color_cap = color.capitalize()
    selected = context["langlaufen_medal_winners"].get(color_cap)
    context = {
        "medal": color_cap,
        "winner": selected
    }
    return render(request, "base/medal.html", context)

def load_indexpage(request):
    return render(request, "base/index.html")

def Distances(requests):
    distances = Distance.objects.all()
    context = {"distances": distances}
    return render(requests, "base/distance.html", context)

def times_by_length(request, length):
    length = request.GET.get('length', length)
    distance = get_object_or_404(Distance, length=length)
    times = Time.objects.filter(distance=distance)

    return render(request, 'base/times_by_length.html', {
        'times': times,
        'length': length,
    })