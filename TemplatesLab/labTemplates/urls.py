from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views


app_name = "labTemplates"



urlpatterns=[

    path("today/", views.todayDate, name="TodayDate"),
    path("random/password/", views.randomPassword, name="randomPassword"),
    path("favs/games/", views.favoriteGames, name="favoriteGames")
]