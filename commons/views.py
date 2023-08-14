from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'commons/index.html', {'signup': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, user=form.get_user())
    else:
        form = AuthenticationForm()
    return render(request, 'commons/index.html', {'login': form})


def about_us(request):
    return render(request, 'commons/about-us.html')
