from django.urls import path
from . import views
app_name="MainPage"

urlpatterns =[
    path('today/',views.TheDate, name="Date"),
    path("random/password", views.randomPassword , name="RandomPassword"),
    path("fav/games",views.favGames,name="FavoiteGames"),
]