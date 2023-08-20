from django.shortcuts import render


def events(request):
    return render(request, 'events/events.html')


def events_detail(request):
    return render(request, 'events/events-detail.html')
