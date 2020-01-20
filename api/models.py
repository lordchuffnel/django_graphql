from django.db import models



class Movie(models.Model):
  title = models.Charfield(max_length=32)
  year = models.IntegerField(default=2000)