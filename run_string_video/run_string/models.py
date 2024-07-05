from django.db import models
from django.utils import timezone


class QueryFromUser(models.Model):
    query_text = models.TextField()
    send_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["send_time"]
        indexes = [
            models.Index(fields=["send_time"])
        ]

    def __str__(self):
        return self.query_text[:20]
