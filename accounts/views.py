from django.shortcuts import redirect
from .forms import RegisterForm


def signin(request):
    pass


def signup(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home_page")
    else:
        print(form.errors)
