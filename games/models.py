from django.db import models
from roomzi.models import BaseModel


class Company(BaseModel):
    name = models.CharField()
    description = models.TextField()
    logo = models.ImageField()

    class Meta:
        verbose_name = 'Company'

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Category'

    def __str__(self):
        return self.name


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

    class Meta:
        verbose_name = 'Games'
    def __str__(self):
        return self.name