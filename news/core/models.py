from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class News(models.Model):
    """Model for news"""
    date = models.DateField(default=timezone.now())
    text = models.TextField(max_length=150)