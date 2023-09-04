from django.db import models
from roomzi.models import BaseModel


class SliderLanding(BaseModel):
    picture = models.ImageField()
    link = models.CharField(max_length=255)
    order = models.IntegerField()


class AboutUs(BaseModel):
    description = models.TextField()


class SocialMedia(BaseModel):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    icon = models.FileField()


class TeamMembers(BaseModel):
    Member_Choices = (
        (1, "Manager"),
        (2, "Front-End programmer"),
        (3, "Back-End programmer")
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.IntegerField(choices=Member_Choices)
    picture = models.ImageField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
