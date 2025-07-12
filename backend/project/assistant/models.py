# assistant/models.py
from django.db import models
from django.contrib.postgres.fields import ArrayField  # use JSONField on SQLite
from django.conf import settings
from django.db import models
from django.utils import timezone


class SwapRequest(models.Model):
    """
    A single skill‑swap proposal from one user (requester) to another (requestee).
    """

    class Status(models.TextChoices):
        PENDING   = "pending", "Pending"
        ACCEPTED  = "accepted", "Accepted"
        REJECTED  = "rejected", "Rejected"
        CANCELLED = "cancelled", "Cancelled"

    # If you store profiles in a StudentProfile model, switch to ForeignKey("core_app.StudentProfile", …)
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="swap_requests_sent",
    )
    requestee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="swap_requests_received",
    )

    offered_skill = models.CharField(max_length=100)
    wanted_skill  = models.CharField(max_length=100)
    status        = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.CheckConstraint(
                check=~models.Q(requester=models.F("requestee")),
                name="requester_and_requestee_cannot_be_same",
            )
        ]

    def __str__(self):
        return f"{self.requester} → {self.requestee} [{self.status}]"


class Course(models.Model):
    """
    Minimal course catalogue for recommendations.
    """
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=100)          # e.g. Coursera
    url = models.URLField()
    description = models.TextField(blank=True)
    skills_taught = ArrayField(models.CharField(max_length=50))   # ["Python","SQL"]
    level = models.CharField(max_length=50)              # Beginner / Intermediate / Advanced
    domain = models.CharField(max_length=100)            # Software / Design / Business …
    rating = models.FloatField(default=4.0)              # 1–5

    def __str__(self):
        return self.title
