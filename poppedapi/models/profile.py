from django.db import models
from .user import User
from .user_genre import User_Genre

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_genre = models.ForeignKey(User_Genre, on_delete=models.CASCADE)
