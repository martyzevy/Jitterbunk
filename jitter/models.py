from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    bunks = models.ManyToManyField('Bunk',related_name='bunked_users')
    
    def __str__(self):
        return self.username

class Bunk(models.Model):
    fromU = models.ForeignKey('User', on_delete=models.CASCADE, related_name="fromUser")
    toU = models.ForeignKey('User', on_delete=models.CASCADE, related_name="toUser")
    time = models.TimeField('Time')

    












