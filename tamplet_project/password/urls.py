from django.urls import path
from . import views

app_name = "random_password"
urlpatterns = [
    path("random/password/", views.random_password, name="random_password"),

    
]