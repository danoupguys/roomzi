from django.urls import path
from . import views

urlpatterns = [
    path("signin/", views.signin, name='signin'),
    path("signup/", views.signup, name='signup'),
    path("profile/", views.profile, name='account_profile'),
    path("edit-password/", views.edit_password, name='edit_password'),
    path("event-history/", views.event_history, name='event_history'),
    path("games-history/", views.games_history, name='games_history'),
    path("support/", views.support, name='support'),
]
