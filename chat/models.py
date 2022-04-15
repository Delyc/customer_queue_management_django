from cProfile import label
from datetime import timezone
from statistics import mode

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255, blank=True)
    label = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(
        Room, related_name="messages", on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
