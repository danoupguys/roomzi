from django.shortcuts import render


def home_page(request):
    return render(request, 'commons/index.html')


def about_us(request):
    return render(request, 'commons/about-us.html')
