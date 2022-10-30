from django.http import HttpRequest
from django.shortcuts import render
from datetime import date
import random

# Create your views here.
#Password = ["1111111","2222222","3333333","4444444"]

def Date_Of_Today(request : HttpRequest):
    Today = {"Date": date.today() }
    return render(request,"templatesweb/date.html", Today)

def Randomly_Password(request: HttpRequest):
    RPL = random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$", k = 15)
    pas = "".join(RPL)
    return render(request, "templatesweb/Password.html", {"Random_Password" : pas})

    #Random_Password ={"Random_Password" : random.choice(Password)}
    #return render(request, "templatesweb/Password.html", Random_Password)

def Favorite_Games(request: HttpRequest):
    Games = {"Games" : ["Game 1", "Game 2", "Game 3"]}
    return render(request, "templatesweb/Games.html", Games)