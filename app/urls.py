from app.views import *
from django.urls import path

app_name = 'app'

urlpatterns = [
    path("", home, name = 'home'),
]