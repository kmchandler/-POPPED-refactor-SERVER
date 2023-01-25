from django.db import models
from .flick import Flick

class Flick_Cast_Crew(models.Model):

    flick = models.ForeignKey(Flick, on_delete=models.CASCADE)
    cast_crew = models.CharField(max_length=100)

    def __str__(self):
        return self.cast_crew
