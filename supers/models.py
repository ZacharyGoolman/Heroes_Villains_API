from django.db import models

class Supers(models.Model):
    name = models.CharField(max_length=200)
    alter_ego = models.CharField(max_length=200)
    primary_ability = models.CharField(max_length=200)
    secondary_ability = models.CharField(max_length=200)
    catchphrase = models.CharField(max_length=200)
    super_type = models.ForeignKey