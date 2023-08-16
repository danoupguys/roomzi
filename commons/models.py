from django.db import models
from roomzi.models import BaseModel


class About_us(BaseModel):
    description = models.TextField()


class Social_media(BaseModel):
    title = models.TextField()
    link = models.TextField()
    icon = models.TextField()
