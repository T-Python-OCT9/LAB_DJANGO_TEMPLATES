from django.urls import path
from . import views

app_name = "favorit games"
urlpatterns = [
    path("fav/games/",views.fav_games ,name="favorit_games"),
    
]