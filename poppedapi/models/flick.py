from django.db import models

class Flick(models.Model):

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    watched = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    image_url = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)
    uid = models.CharField(max_length=100)

    def __str__(self):
        return self.title
