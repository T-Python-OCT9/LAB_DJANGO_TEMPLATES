from django.urls import path
from .views import todayView, random_password, favoriteGamesView

app_name ='website'

urlpatterns =[
    path('today/' ,todayView , name='today'),
    path('random/password/',random_password, name="random_pass"),
    path('favs/games/' , favoriteGamesView, name='games'),

]