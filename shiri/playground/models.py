from django.db import models

class Guess(models.Model):
    number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
