from django.shortcuts import render
from django.http import HttpRequest
from datetime import date
import string
import random

# Create your views here.
def todayView(request : HttpRequest):
    context = {'date': date.today}
    return render(request, 'website/my.html',  context)


def random_password(request : HttpRequest):

    random_pass_list = random.choices(string.ascii_letters+string.digits+string.punctuation, k=15)
    random_pass_str = "".join(random_pass_list)

    return render(request, 'website/my.html', {"pass" : random_pass_str})


def favoriteGamesView(request: HttpRequest):
    favorite_games =['game' , 'bpg' , 'lkm']
    context ={'favorite_games' : favorite_games}
    return render(request , 'website/my.html' , context)


