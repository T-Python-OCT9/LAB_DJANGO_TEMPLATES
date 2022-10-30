from unicodedata import name
from . import views
from django.urls import path

app_name ="app2"

urlpatterns = [
    path('date/',views.today,name= "date"),
    path('password/',views.passworrd,name= "random pass")
]
