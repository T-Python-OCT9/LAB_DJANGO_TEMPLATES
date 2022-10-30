from multiprocessing import context
from django.shortcuts import render
from datetime import date
from random import randint
from django.http import HttpRequest, HttpResponse

def Datetoday(request : HttpRequest):
    context = {"todayDate": date.today() }
    return render (request , "timp_html/data.html" , context)
def random_pass (request : HttpRequest):
    password = ''
    for i in range (0,10):
        password += (randint(0,10))
    context = {"pass" : password}
    return render (request , "timp_html/Randmnum.html" , context) 

def myfave_games(request : HttpRequest):
    context = {"Fave_Games" :  ["battlefield" , "Sekiro", "fifa"]}
    return render ( request , "timp_html/games.html" , context)


