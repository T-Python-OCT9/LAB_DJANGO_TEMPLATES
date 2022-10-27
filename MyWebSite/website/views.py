from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date

# Create your views here.

def theDate(request : HttpRequest):
    context = {'todayDate' : date.today}
    return render(request, "website\index.html", context)