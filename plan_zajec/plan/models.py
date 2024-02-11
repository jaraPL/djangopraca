from django.db import models


class Plan(models.Model):
    day = models.CharField(max_length=20)
    time = models.TimeField()
    activity = models.CharField(max_length=100)