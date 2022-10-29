from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
from password_generator import PasswordGenerator

# Create your views here.

def theDate(request : HttpRequest):
    context = {'todayDate' : date.today}
    return render(request, "website\index.html", context)

def passwordGenerator(request : HttpRequest):
    pow = PasswordGenerator()
    context = {'password' : pow.generate}
    return render(request, "website\password.html", context)

def favGames(request : HttpRequest):
    context = {'fav_games' : ["pac man", "flap jack", "mario", "horizon"]}
    return render(request, "website\FavGames.html", context)