from django.db import models
from roomzi.models import BaseModel


class AboutUs(BaseModel):
    description = models.TextField()


class SocialMedia(BaseModel):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    icon = models.ImageField()


class TeamMembers(BaseModel):
    Member_Choices = (
        (1, "Manager"),
        (2, "Front end programmer"),
        (3, "Backend programmer")
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.IntegerField(choices=Member_Choices)
    picture = models.ImageField()
