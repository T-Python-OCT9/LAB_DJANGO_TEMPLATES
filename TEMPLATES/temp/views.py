from multiprocessing import context
import string
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random

# Create your views here.
def Datetoday(request : HttpRequest):
    context = {'date': date.today()}
    return render(request,'tempdata/date.html' ,context)

def myfave_games(request: HttpRequest):
    favorite_games = ['GRAND', 'FIFA']
    context = {'favorite_games' : favorite_games}
    return render(request, 'tempdata/favsgames.html', context)

def random_pass(request : HttpRequest):

    random_pass_list = random.choices(string.ascii_letters+string.digits+string.punctuation, k=15)
    random_pass_str = "".join(random_pass_list)

    return render(request, 'tempdata/randompass.html', {"pass" : random_pass_str})
