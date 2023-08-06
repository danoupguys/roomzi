from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.games, name='games'),
    path('games-data/', views.games_data, name='games-data')
]
