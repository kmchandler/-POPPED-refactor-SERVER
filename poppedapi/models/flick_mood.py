from django.db import models
from models import Flick, Mood

class Flick_Genre(models.Model):

    flick_id = models.ForeignKey(Flick, on_delete=models.CASCADE)
    mood_id = models.ForeignKey(Mood, on_delete=models.CASCADE)

    def __str__(self):
        return self.mood_id
