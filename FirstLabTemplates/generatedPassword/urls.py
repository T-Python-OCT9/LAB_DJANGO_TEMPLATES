from generatedPassword import views
from django.urls import path

app_name="generatedPassword"


urlpatterns=[
    path("Password/",views.generatedPassword,name="generatedPassword")
]