from django.db import models
from .flick import Flick

class Flick_Recommended_By(models.Model):

    flick_id = models.ForeignKey(Flick, on_delete=models.CASCADE)
    recommended_by = models.CharField(max_length=100)

    def __str__(self):
        return self.recommended_by
