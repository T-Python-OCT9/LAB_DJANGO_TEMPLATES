from datetime import datetime
from operator import truediv
import string
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
import random


# Create your views here.


def fav_games(request: HttpRequest):
    context={"favgames" : ['XO','football','online games']
    }
    return render(request, "app2/index2.html", context)

def today_date(request: HttpRequest):
    context={"today": datetime.today()}
    
    return render(request, "app2/index.html", context)


def randompass(request: HttpRequest):
    context={"randompass": randompass1()}
    
    return render(request, "app2/index3.html", context)
    


def randompass1():
    pas=''
    pas_len=8

    for i in range(pas_len) :
        pas+=''.join(random.choice(string.printable))
        
    
    return(pas)

        

