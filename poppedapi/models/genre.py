from django.db import models

class Genre(models.Model):

    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.genre_name
