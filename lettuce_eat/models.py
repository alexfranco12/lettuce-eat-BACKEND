from django.db import models

class Restaurant(models.Model):
  name = models.CharField(max_length=50)
  summary = models.TextField(blank=True, null=True)
  website = models.CharField(max_length=200, blank=True, null=True)
  image_url = models.TextField()

  def __str__(self):
    return self.name