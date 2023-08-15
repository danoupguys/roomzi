from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render


def signin(request):
    pass


def signup(request):
    return HttpResponse('signup')
