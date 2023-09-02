from django.shortcuts import render
from games.models import Games
from commons.models import SocialMedia


def home_page(request):
    games_landing = Games.objects.all()
    return render(request, 'commons/index.html', {'games': games_landing})


def about_us(request):
    social_media = SocialMedia.objects.all()
    return render(request, 'commons/about-us.html', {'SocialMedia': social_media})
