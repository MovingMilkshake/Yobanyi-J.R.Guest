from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    thumbnail = models.ImageField(null=True, blank=True, upload_to='thumbnails/')
    text = models.TextField()
