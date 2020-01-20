from django.db import models



class Movie(models.Model):
  title = models.CharField(max_length=32)
  year = models.IntegerField(default=2000)

  def __str__(self):
    return self.title