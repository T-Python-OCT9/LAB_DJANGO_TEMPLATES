from multiprocessing import context
from django.shortcuts import render
import datetime 
import secrets
from django.http import HttpRequest, HttpResponse


def today_date(request : HttpRequest): 
   context = {"today_date" :datetime.date.today(), "Current_time" : datetime.datetime.now()}
   return render( request, 'lab/today.html' ,context)
  
  
def Pass_generate(request : HttpRequest):

  password_length = 8
  random_pass = secrets.token_urlsafe(password_length)
  context = {"random_password" : random_pass}
  return render (request , "lab/pass.html" , context) 

def fave_games(request : HttpRequest):
    context = {"Favorite_Games" :  ["hi_Day" , "minecraft", "escape"]}
    return render ( request , "lab/games.html" , context)


