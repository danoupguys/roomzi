from django.shortcuts import render
from games.models import Games
from commons.models import SocialMedia, TeamMembers, AboutUs, SliderLanding


def home_page(request):
    sliders = SliderLanding.objects.all().order_by('order')
    games_landing = Games.objects.all()
    return render(request, 'commons/index.html', {'games': games_landing, 'sliders': sliders})


def about_us(request):
    aboutus = AboutUs.objects.all()
    team_members = TeamMembers.objects.all()
    social_media = SocialMedia.objects.all()
    return render(request, 'commons/about-us.html',
                  {'SocialMedia': social_media, 'TeamMembers': team_members, 'AboutUs': aboutus})
