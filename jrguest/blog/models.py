from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='thumbnails/')
    text = models.TextField()

    @staticmethod
    def get_absolute_url():
        return reverse('blog_page')
