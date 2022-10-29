from django.urls import path     
from . import views


urlpatterns = [
    path('today/', views.today, name="today"),
    path('random/password/', views.password, name="password"),
    path('favs/games/', views.favGames, name="games"),
]