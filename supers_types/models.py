from django.db import models
from django.forms import CharField



class Super_Types(models.Model):
    type = models.CharField(max_length=200)
