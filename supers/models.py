from tkinter import CASCADE
from django.db import models
from supers_types.models import Super_Types


class Supers(models.Model):
    name = models.CharField(max_length=200)
    alter_ego = models.CharField(max_length=200)
    primary_ability = models.CharField(max_length=200)
    secondary_ability = models.CharField(max_length=200)
    catchphrase = models.CharField(max_length=200)
    supers_type = models.ForeignKey(Super_Types, on_delete=models.CASCADE)