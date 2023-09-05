from django.db import models
from games.models import Games
from roomzi.models import BaseModel
from django.contrib.postgres.fields import DateRangeField, DateTimeRangeField
from accounts.models import CustomUser


class Event(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    register_duration_time = DateRangeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    picture = models.ImageField()
    user_limit = models.IntegerField()
    capacity = models.IntegerField()
    price = models.IntegerField()
    rate = models.PositiveIntegerField()
    game = models.ForeignKey(Games, on_delete=models.CASCADE)


class Slider(BaseModel):
    title = models.CharField(max_length=255)
    picture = models.ImageField()
    link = models.CharField(max_length=255)
    order = models.IntegerField()


class Reservestion(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
