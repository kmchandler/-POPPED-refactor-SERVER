from django.db import models
from models import Mood

class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    image_url = models.CharField(max_length=1000)
    uid = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name
