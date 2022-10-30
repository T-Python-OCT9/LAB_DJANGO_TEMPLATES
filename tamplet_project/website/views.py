import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import string ,random 


games_list=["Zelda:breath of the wild","last of us","horizon","final fantasy"]
# Create your views here.
def today(request : HttpRequest):
    today=date.today()
    context={
        "today":f"today date is:<br> {today}"
    }
       
    return render (request,"website/index.html",context)




