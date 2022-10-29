from django.urls import path
from . import views
app_name="app2"

urlpatterns = [
    path("today/", views.today_date, name="today_date"),
    path("favs/games/", views.fav_games, name="fav_games"),
    path("random/password/", views.randompass, name="randompass")
]