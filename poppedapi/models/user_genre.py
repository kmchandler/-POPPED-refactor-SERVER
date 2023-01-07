from django.db import models
from .user import User
from .genre import Genre

class User_Genre(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
