from django.db import models
from models import Flick, User

class User_Flick(models.Model):

    flick_id = models.ForeignKey(Flick, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id