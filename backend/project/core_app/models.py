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


class SwapRequest(models.Model):
    REQUEST_STATUS = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    ]

    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_requests")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_requests")
    skill_offered = models.CharField(max_length=100)
    skill_requested = models.CharField(max_length=100)

    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=REQUEST_STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.requester.username} → {self.receiver.username} | {self.status}"
