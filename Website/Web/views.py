import string
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from datetime import date
import random
# Create your views here.

def tody_date(request : HttpRequest):
   
    context = {"currentDate" : date.today()}
    return render( request,"Website/todaydate.html",context)



def random_Pass(request : HttpRequest):

  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(12))
  context = {"pass" : password}
  return render(request , "Website/pass.html" , context)


def fav_Games(request : HttpRequest):
    context = { "favGame":["super mario" , "crash bandicoot" ,"pepsiman"] }
    return render (request , "Website/favGame.html" , context)