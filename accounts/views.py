from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import RegisterForm
from django.shortcuts import render


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, user=form.get_user())
            return redirect('home_page')
        else:
            return HttpResponse("<h1>ridi</h1>")


def signup(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home_page")
    else:
        print(form.errors)


def profile(request):
    return render(request, 'accounts/profile.html')


def edit_password(request):
    return render(request, 'accounts/edit_password.html')

