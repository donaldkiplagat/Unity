from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

import datetime as dt

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name
