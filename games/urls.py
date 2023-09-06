from django.urls import path
from . import views

urlpatterns = [
    path('', views.games, name='games'),
    path('<int:game_id>/', views.games_data, name='games_data'),
    path('result/', views.result, name='result')
]
