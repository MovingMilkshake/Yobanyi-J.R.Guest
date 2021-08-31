from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.TextField()
    description = models.TextField()
    date = models.DateField()
