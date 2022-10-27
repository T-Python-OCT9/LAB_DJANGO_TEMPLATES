from django.shortcuts import render
from django.http import HttpRequest
from datetime import date
import string

# Create your views here.
def todayView(request : HttpRequest):
    context = {'date': date.today}
    return render(request, 'website/my.html', context)


def randomPasswordView(request :HttpRequest):
    type_of_password =string.ascii_lowercase+ string.ascii_uppercase + string.digits
    password= ''.join(random.choice(type_of_password)for i in range (10))
    context = {'password':password}
    return render(request,'website/my.html', context)


def favoriteGamesView(request: HttpRequest):
    favorite_games =['game1' , 'game2' , 'game3']
    context ={'favorite_games' : favorite_games}
    return render(request , 'website/my.html' , context)


