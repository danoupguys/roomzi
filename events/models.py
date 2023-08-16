from django.db import models
from roomzi.models import BaseModel
from django.contrib.postgres.fields import DateRangeField, DateTimeRangeField


# Create your models here.
class Event(BaseModel):
    title = models.TextField()
    description = models.TextField()
    register_duration_time = DateRangeField()  # date range
    game_duration_time = DateTimeRangeField()  # date time range
    picture = models.TextField()
    user_limit = models.IntegerField()
    capacity = models.IntegerField()
    price = models.IntegerField()
    rate = models.PositiveIntegerField()


class Slider(BaseModel):
    title = models.TextField()
    picture = models.TextField()
    link = models.TextField()
    order = models.IntegerField()


class Reservestion(BaseModel):
    user_id = models.IntegerField()
    status = models.IntegerField()
    event_id = models.IntegerField()
