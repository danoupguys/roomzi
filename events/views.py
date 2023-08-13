from django.shortcuts import render


# Create your views here.
def events(request):
    return render(request, 'events/events.html')


def events_detail(request):
    return render(request, 'events/events-detail.html')
