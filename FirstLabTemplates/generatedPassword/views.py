
from unittest import result
from django.shortcuts import render
from django.http import HttpRequest
import random
import string



letters = f"{string.ascii_letters}{string.digits}"

list_pas=[random.choice(letters),random.choice(letters),random.choice(letters),random.choice(letters),random.choice(letters),random.choice(letters),random.choice(letters),random.choice(letters),random.choice(letters),random.choice(letters),random.choice(letters)]


def generatedPassword (request : HttpRequest):
    context = {
        "generatedPassword" : list_pas
        }
    return render(request, "generatedPassword/index.html" , context)


# Create your views here.
