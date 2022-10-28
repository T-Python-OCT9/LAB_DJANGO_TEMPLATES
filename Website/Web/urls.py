from django.urls import path
from . import views

app_name = "Website"

urlpatterns = [
    path("today/", views.tody_date, name = "tody_date"),
    path("random/password/", views.random_Pass, name="random_Pass"),
    path("favs/games/", views.fav_Games, name="fav_Games")

]