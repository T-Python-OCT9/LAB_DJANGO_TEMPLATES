from multiprocessing import context
from django.shortcuts import render
from datetime import date
import random 
from django.http import HttpRequest, HttpResponse
import string
def Datetoday(request : HttpRequest):
    context = {"todayDate": date.today() }
    return render (request , "timp_html/data.html" , context)

def random_pass (request : HttpRequest):
    password = ''
    cr = string.ascii_letters+ string.digits
    for i in range (10):
        password += random.choice(cr)
    context = {"pass" : password}
    return render (request , "timp_html/Randmnum.html" , context) 

def myfave_games(request : HttpRequest):
    context = {"Fave_Games" :  ["battlefield" , "Sekiro", "fifa"]}
    return render ( request , "timp_html/games.html" , context)


