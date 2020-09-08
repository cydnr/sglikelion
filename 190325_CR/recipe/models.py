from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now)
    writer = models.TextField(default="")
    ingredients = models.TextField(default="")
    body = models.TextField(default="")
    
