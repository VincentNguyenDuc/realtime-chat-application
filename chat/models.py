from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    million = 10 ** 6
    value = models.CharField(max_length=million)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=million)
    room = models.CharField(max_length=million)
