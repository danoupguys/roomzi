from django.shortcuts import render
from games.models import Games


def home_page(request):
    games_aray = Games.objects.all()
    return render(request, 'commons/index.html', {'commons': games_aray})


def about_us(request):
    return render(request, 'commons/about-us.html')
