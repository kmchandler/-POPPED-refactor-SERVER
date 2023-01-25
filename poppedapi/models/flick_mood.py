from django.db import models
from .flick import Flick
from .mood import Mood

class Flick_Mood(models.Model):

    flick = models.ForeignKey(Flick, on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
