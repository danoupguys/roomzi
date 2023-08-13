from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.events),
    path("events-detail/", views.events_detail)
]
