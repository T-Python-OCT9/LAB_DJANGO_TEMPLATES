from django.urls import path
from .views import todayView, randomPasswordView, favoriteGamesView

app_name ='website'

urlpatterns =[
    path('today/' ,todayView , name='today'),
    path('random/password/' , randomPasswordView , name='random_password'),
    path('favs/games/' , favoriteGamesView, name='favorite_games'),

]