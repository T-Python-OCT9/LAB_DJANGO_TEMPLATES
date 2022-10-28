from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import date






def today (request : HttpRequest):
    context = {
        "date" : date.today()
        }
    return render(request, "Today/index.html" , context)





# Create your views here.


