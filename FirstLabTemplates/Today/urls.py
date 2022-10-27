from . import views
from django.urls import path

app_name="Today"


urlpatterns=[
    path("today/",views.today,name="today")
]