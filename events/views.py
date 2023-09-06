import jdatetime

from django.shortcuts import render

from events.models import Event


def events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events.html', {'events': event_list})


def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)

    datetime_upper = jdatetime.datetime.fromgregorian(datetime=event.register_duration_time.upper, locale='fa_IR')
    datetime_lower = jdatetime.datetime.fromgregorian(datetime=event.register_duration_time.lower, locale='fa_IR')

    register_duration_time_str = (f"از تاریخ {datetime_lower.day}"
                                  f" {jdatetime.date.j_months_fa[datetime_upper.month - 1]} تا "
                                  f"{datetime_upper.day} {jdatetime.date.j_months_fa[datetime_lower.month - 1]}")

    return render(request, 'events/events-detail.html',
                  {'event_detail': event, 'register_duration_time_str': register_duration_time_str})
