from django.db import models
from models import User, Genre

class User_Genre(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id
