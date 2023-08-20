from django.db import models
from roomzi.models import BaseModel


class AboutUs(BaseModel):
    description = models.TextField()


class SocialMedia(BaseModel):
    title = models.TextField()
    link = models.TextField()
    icon = models.TextField()


class TeamMembers(BaseModel):
    Member_Choices = (
        (1, "مدیر"),
        (2, "برنامه نویس فرانت"),
        (3, "برنامه نویس بک اند")
    )
    first_name = models.TextField()
    last_name = models.TextField()
    role = models.IntegerField(choices=Member_Choices)
    picture = models.TextField()
