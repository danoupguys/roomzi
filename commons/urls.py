from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page),
    path("about-us/", views.about_us, name="about_us"),
]
