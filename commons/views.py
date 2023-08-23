from django.shortcuts import render
from games.models import Games


def home_page(request):
    games_landing = Games.objects.all()
    return render(request, 'commons/index.html', {'commons': games_landing})


def about_us(request):
    return render(request, 'commons/about-us.html')
