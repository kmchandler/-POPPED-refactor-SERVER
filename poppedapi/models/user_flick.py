from django.db import models
from .flick import Flick
from .user import User

class User_Flick(models.Model):

    flick = models.ForeignKey(Flick, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
