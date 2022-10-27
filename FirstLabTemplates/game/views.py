from django.shortcuts import render
from django.http import HttpRequest,HttpResponse




list_game=["Game1","Game2","Game3","Game4"]

def favorite_game (request : HttpRequest):
    context = {
        "game" : list_game
        }
    return render(request, "game/index.html" , context)



# Create your views here.
