from django.db import models
from models import Flick_Mood, Flick_Cast_Crew, Flick_Genre, Flick_Recommended_By

class Flick(models.Model):

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    flick_genres = models.ForeignKey(Flick_Genre, on_delete=models.CASCADE) 
    flick_moods = models.ForeignKey(Flick_Mood, on_delete=models.CASCADE)
    cast_crew = models.ForeignKey(Flick_Cast_Crew, on_delete=models.CASCADE) 
    recommended_by = models.ForeignKey(Flick_Recommended_By, on_delete=models.CASCADE) 
    watched = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    image_url = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)
    uid = models.CharField(max_length=100)

    def __str__(self):
        return self.title
