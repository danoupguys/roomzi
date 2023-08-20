from django.db import models
from roomzi.models import BaseModel


class Games(BaseModel):
    name = models.TextField()
    company_id = models.IntegerField()
    min_user = models.IntegerField()
    max_user = models.IntegerField()
    min_age = models.IntegerField()
    category = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    picture = models.TextField()
    rate = models.IntegerField()


class Company(BaseModel):
    name = models.TextField()
    description = models.TextField()
    logo = models.TextField()


class Category(BaseModel):
    name = models.TextField()
    description = models.TextField()
