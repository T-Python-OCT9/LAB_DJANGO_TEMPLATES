from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views

app_name = "my_app"


urlpatterns = [
    path('today/', views.today_date, name="today_date"),
    path('random/password', views.randomly_password, name="randomly_password"),
    path('favs/games/', views.favorite_games, name="favorite_games"),
]
