from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tune(models.Model):
    vextab = models.TextField()
    answer = models.CharField(max_length=100)
    link = models.URLField(max_length=100)
    date = models.DateField(auto_now_add=True, primary_key=True)

    successful_guessers = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f'{self.date}'
