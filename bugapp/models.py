from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class MyUser(AbstractUser):
    pass

class Ticket(models.Model):
    NEW = 'N'
    COMPLETE = 'C'
    IN_PROGRESS = 'P'
    INVALID = 'I'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (COMPLETE, 'Complete'),
        (IN_PROGRESS, 'In Progress'),
        (INVALID, 'Invalid'),
    ]

    title = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=500)
    filed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    ticket_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="assigned_to", blank=True, null=True)
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="completed_by", blank=True, null=True)

    def __str__(self):
        return self.title
