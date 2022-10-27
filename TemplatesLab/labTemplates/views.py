from django.http import HttpRequest
from django.shortcuts import render
from datetime import date
from random import randint

# Create your views here.


def todayDate(request : HttpRequest):
    context = {"todayDate": date.today() }
    return render(request,"labTempl/date.html", context)

def randomPassword(request: HttpRequest):
    password = ""
    for i in range(0,9):
        password += str(randint(0,9))
    context = {"pass" : password}
    return render(request, "labTempl/randomPass.html", context)
        


def favoriteGames(request: HttpRequest):

    context = {"favGames" : ["League of legends", "Rocket leageue", "WoW"]}

    return render(request, "labTempl/favGames.html", context)

