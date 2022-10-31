from django.urls import path
from . import views

app_name = "proj_Temp"

urlpatterns = [
    path("today/", views.Datetoday ,name = "todayDate"),
    path("random/password/", views.random_pass, name = "Pass"),
    path("favs/games/", views.myfave_games, name = "Fave_Games")
]