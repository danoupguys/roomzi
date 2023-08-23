from django.shortcuts import render
from events.models import Event


def events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events.html', {'events': event_list})


def events_detail(request):
    return render(request, 'events/events-detail.html')
