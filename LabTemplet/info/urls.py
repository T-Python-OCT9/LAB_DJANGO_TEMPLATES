from django.urls import path
from . import views

app_name = "info"

urlpatterns = [ 
         path(" ", views.information),
         path(" ", views.random_pass),
         path(" ", views.game),
]