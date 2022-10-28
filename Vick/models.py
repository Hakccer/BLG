from django.db import models

# Create your models here.

class Calors(models.Model):
    link = models.TextField()
    title = models.TextField()
    desc = models.TextField()
    slug = models.SlugField(unique=True, blank=False)
    content = models.TextField()
    dats = models.DateField()
