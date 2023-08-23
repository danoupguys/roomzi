from django.shortcuts import render
from games.models import Games


def games(request):
    games_list = Games.objects.all()
    return render(request, 'games/Games.html', {'games': games_list})


def games_data(request):
    return render(request, 'games/Games-data.html')
