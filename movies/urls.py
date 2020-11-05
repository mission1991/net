from django.urls import path
from .views import *

app_name = 'movies'

urlpatterns = [
    path('', movie_in_category, name='movie_in_category'),
    path('<int:id>/<movie_slug>/', movie_detail, name='movie_detail'),
]