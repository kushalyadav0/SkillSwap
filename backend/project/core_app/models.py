from django.db import models
from django.contrib.auth.models import User

AVAILABILITY_CHOICES = [
    ("weekends", "Weekends"),
    ("evenings", "Evenings"),
    ("anytime", "Anytime"),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default="anytime")
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.name or self.user.username
