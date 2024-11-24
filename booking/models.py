from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    location = models.TextField()

    def __str__(self):
        return f'{self.number}'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', default=None)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings', default=None)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}:{self.room}'
