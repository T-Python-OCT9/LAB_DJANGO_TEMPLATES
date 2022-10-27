from . import views
from django.urls import path

app_name="game"


urlpatterns=[
    path("game/",views.favorite_game,name="game")
]