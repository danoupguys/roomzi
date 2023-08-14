from django.db import models
from roomzi.models import BaseModel


# Create your models here.
class Games(BaseModel):
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    logo = models.TextField()


class Category(BaseModel):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
