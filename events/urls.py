from django.urls import path
from . import views

urlpatterns = [
    path("", views.events, name='event'),
    path("<int:event_id>/", views.events_detail, name='event_detail')
]
