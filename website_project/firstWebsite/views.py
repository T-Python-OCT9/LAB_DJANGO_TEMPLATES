from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import string
import random

# Create your views here.

def get_date(request: HttpRequest): 
    context = {'date_today': date.today()}
    return render(request, "firstWebsite/datePage.html", context)

def random_password(request: HttpRequest):
    characters = f'{string.ascii_letters}{string.digits}{string.punctuation}' 
    password = ""
    for i in range(9):
        char = random.choice(characters)
        password += char
    context = {'password' : password}
    return render(request, "firstWebsite/passwordPage.html", context)
   
def favs_games(request : HttpRequest):
    context = {
        'games' : ['Call Of Duty','FIFA','RED DEAD','GTA','Butterfield']
    }
    return render(request, "firstWebsite/games.html", context)
    
