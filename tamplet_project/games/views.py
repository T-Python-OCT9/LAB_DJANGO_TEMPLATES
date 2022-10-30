from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def fav_games (request:HttpRequest):
    context ={
        "game_list" : ["Zelda:breath of the wild","last of us","horizon","final fantasy"]
        } 
    return render (request,"games/index.html",context)