from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string ,random 
# Create your views here.
def random_password(request : HttpRequest):
    source = string.ascii_letters + string.digits
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(source) for i in range(16))
    context={
        "random_pass": result_str
    }
    
    return render(request,"password/index.html",context)