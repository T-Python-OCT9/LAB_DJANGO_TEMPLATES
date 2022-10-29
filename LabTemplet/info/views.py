from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
from random import choice
import string

# Create your views here.

def information(request: HttpRequest):
    date_today = datetime.datetime.now().date

    return HttpResponse(date_today)

#print(information(1))    



def random_pass(request: HttpRequest):
    
    p = ""
    char = list(string.ascii_letters + string.digits + '!@#$%^&*')
     
    while len(p) <= 8:
        p += choice(char)
        

    return HttpResponse(p) 

#print(random_pass(8))



list_of_game =["puzzles","crush","solitaire","farm"]

def game(request: HttpRequest):

    for i in list_of_game:
      output += list_of_game[i]
    
    return HttpResponse(output)

#print(game(list_of_game))    