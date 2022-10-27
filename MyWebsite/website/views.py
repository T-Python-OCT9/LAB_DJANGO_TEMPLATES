from django.shortcuts import render
from django.http import HttpRequest
from datetime import date
import random, string

# Create your views here.
def todayView(request: HttpRequest):
    context = {'date': date.today}
    return render(request, 'website/date.html', context)

def randomPasswordView(request: HttpRequest):
    types_of_password = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(types_of_password) for i in range(13))
    context = {'password': password}
    return render(request, 'website/password.html', context)


def favoriteGamesView(request: HttpRequest):
    favorite_games = ['Battle Field', 'Fortnite', 'FIFA Ultimate Team']
    context = {'favorite_games' : favorite_games}
    return render(request, 'website/favorite_games.html', context)