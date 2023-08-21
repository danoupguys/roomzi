from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.events, name='event'),
    path("events-detail/", views.events_detail)
]
