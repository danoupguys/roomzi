from django.urls import path
from . import views

urlpatterns = [
    path("", views.events, name='event'),
    path("events-detail/", views.events_detail)
]
