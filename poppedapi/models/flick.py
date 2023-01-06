from django.db import models
from models import Flick_Mood

class Flick(models.Model):

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    moods = models.ForeignKey(Flick_Mood, on_delete=models.CASCADE)
    castCrew = models.CharField(max_length=100) #HOW DO I DO THIS PART??
    recommended_by = models.CharField(max_length=50)
    watched = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    image_url = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)
    uid = models.CharField(max_length=100)

    def __str__(self):
        return self.title
