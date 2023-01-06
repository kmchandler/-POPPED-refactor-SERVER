from django.db import models

class Friend(models.Model):

    friend_id = models.CharField(max_length=100)
    uid = models.CharField(max_length=100)

    def __str__(self):
        return self.friend_id
