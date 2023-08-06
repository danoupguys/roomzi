from django.shortcuts import render


# Create your views here.
def games(request):
    return render(request, 'games/Games.html')


def games_data(request):
    return render(request, 'games/Games-data.html')
