
from multiprocessing import context
from random import random
import string
from django.shortcuts import render
from datetime import date
from django.http import HttpRequest , HttpResponse 
# Create your views here.


def today (request : HttpRequest):
    context ={ 
      "k": date.today()
         }
    return render (request ,"app2/date.html",context )

def passworrd (request : HttpRequest):
    random_pass_list = random.choices(string.ascii_letters+string.digits+string.punctuation, k=12)
    random_pass_str ="".join(random_pass_list)
    return render (request , 'books/random_password.html', {"pass": random_pass_str})

    