from django.db import models


class Reminder(models.Model):
    email = models.EmailField()
    text = models.TextField()
    reminder_time = models.DateTimeField()
