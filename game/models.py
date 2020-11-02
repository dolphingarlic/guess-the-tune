from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tune(models.Model):
    vextab = models.TextField()
    source = models.JSONField()
    date = models.DateField(auto_now_add=True, primary_key=True)

    successful_guessers = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.date}'
