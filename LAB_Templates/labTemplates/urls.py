from django.urls import path
from . import views

app_name = "Lab_Templates"

urlpatterns = [
    path("today/", views.today_date, name = "TodayDate"),
    path("random/password/", views.Pass_generate, name = "Password"),
    path("favs/games/", views.fave_games, name = "Games")

    
 
]