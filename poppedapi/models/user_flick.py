from django.db import models
from .flick import Flick
from .user import User

class User_Flick(models.Model):

    flick_id = models.ForeignKey(Flick, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
