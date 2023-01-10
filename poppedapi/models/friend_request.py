from django.db import models
from .user import User

class Friend_Request(models.Model):

    uid = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
