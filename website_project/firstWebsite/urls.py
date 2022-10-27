from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('today/',views.get_date, name = 'date'),
    path('random/password/',views.random_password, name = 'password'),
    path('favs/games/',views.favs_games, name = 'games')

]