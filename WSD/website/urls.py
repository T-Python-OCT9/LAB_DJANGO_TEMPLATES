from django.urls import path
from . import views


app_name = "website"



urlpatterns=[

    path("today/", views.Date_Of_Today, name="Date_Of_Today"),
    path("random/password/", views.Randomly_Password, name="Randomly_Password"),
    path("favs/games/", views.Favorite_Games, name="Favorite_Games")
]