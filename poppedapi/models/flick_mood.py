from django.db import models
from .flick import Flick
from .mood import Mood

class Flick_Mood(models.Model):

    flick_id = models.ForeignKey(Flick, on_delete=models.CASCADE)
    mood_id = models.ForeignKey(Mood, on_delete=models.CASCADE)

    def __str__(self):
        return self.mood_id
