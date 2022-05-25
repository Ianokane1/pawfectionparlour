import uuid
from django.db import models
# Import Django authentication user system
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Booking Requested"), (1, "Booking Accepted"))


class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings")
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    booking_comments = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-booking_date']


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dog_name = models.CharField(max_length=140)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return str(self.user)        