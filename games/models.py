from django.db import models
from roomzi.models import BaseModel


class Company(BaseModel):
    name = models.TextField()
    description = models.TextField()
    logo = models.TextField()


class Category(BaseModel):
    name = models.TextField()
    description = models.TextField()


class Games(BaseModel):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    min_user = models.IntegerField()
    max_user = models.IntegerField()
    min_age = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    picture = models.ImageField()
    rate = models.SmallIntegerField()
