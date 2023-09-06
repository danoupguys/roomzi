from django.shortcuts import render
from games.models import Games


def games(request):
    games_list = Games.objects.all()
    return render(request, 'games/Games.html', {'games': games_list})


def games_data(request, game_id):
    games_detail = Games.objects.get(id=game_id)
    return render(request, 'games/Games-data.html', {'games_details': games_detail})


def result(request):
    search_term = ''
    if 'searchbar' in request.GET:
        search_term = request.GET['searchbar']
        results = Games.objects.all().filter(name__contains=search_term)
    return render(request, 'games/result.html', {'results': results})
