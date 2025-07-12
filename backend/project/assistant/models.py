# assistant/models.py
from django.db import models
from django.contrib.postgres.fields import ArrayField  # use JSONField on SQLite

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
