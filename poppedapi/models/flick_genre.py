from django.db import models
from models import Flick, Genre

class Flick_Genre(models.Model):

    flick_id = models.ForeignKey(Flick, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.genre_id
