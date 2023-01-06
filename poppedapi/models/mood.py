from django.db import models

class Mood(models.Model):

    mood_name = models.CharField(max_length=50)

    def __str__(self):
        return self.mood_name
