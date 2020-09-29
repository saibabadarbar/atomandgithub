from django.db import models
from django import forms

class Devotee(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    Feedback=models.CharField(max_length=264)

    def __str__(self):
        return self.name
