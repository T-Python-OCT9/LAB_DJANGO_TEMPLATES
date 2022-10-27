import random
import string
from django.http import HttpRequest
from datetime import date, datetime
from django.shortcuts import render
# HttpResponse
# Create your views here.

# This should display the date of today .


def today_date(request: HttpRequest):
    currentdate = datetime.today()
    formatDate = currentdate.strftime("%d-%b-%y")
   #context = {"today_date": date.today()}

    return render(request, "my_app/date.html", {'currentdate': currentdate, 'formatDate': formatDate})


# This should display a randomly generated password .


def randomly_password(request: HttpRequest):
    password = ''.join(random.choice(string.printable) for i in range(8))

    return render(request, "my_app/password.html", {'password': password})

# This should display a list of your favorite games.


def favorite_games(request: HttpRequest):
    context = {"favoritegame": ['last of us', 'witcher', 'call of duty']}

    return render(request, "my_app/favorite_game.html", context)
