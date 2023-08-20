from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import RegisterForm


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
