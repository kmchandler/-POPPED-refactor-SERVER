from django.db import models
from .flick import Flick
from .genre import Genre

class Flick_Genre(models.Model):

    flick_id = models.ForeignKey(Flick, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
