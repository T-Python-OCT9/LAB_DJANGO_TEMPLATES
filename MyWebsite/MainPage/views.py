from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import date 
import random
import string


# Create your views here.
def TheDate(request: HttpRequest):
    ''' this fuction will print today's date'''
    content = {'todayDate':date.today}
    return render(request, "MainPage\index.html",content)

def randomPassword(request:HttpRequest):
    ''' this fuction will print random password'''
    characters = f'{string.ascii_letters}{string.digits}{string.punctuation}' 
    password = ""
    for i in range(9):
        char = random.choice(characters)
        password += char
    context = {'Password' : password} 
    return render(request, "MainPage/RandomPass.html", context)

def favGames(request:HttpRequest):
    ''' this fuction will print my favoite games'''
    context = { 'favgame':["genshin Impact","Cooking Mama","Fruit Ninja","Uno"] } 
    return render (request, "MainPage\FavGame.html", context)
