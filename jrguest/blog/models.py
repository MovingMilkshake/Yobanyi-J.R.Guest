from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('create_post_page')


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='Website Development')
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='thumbnails/')
    text = models.TextField()

    @staticmethod
    def get_absolute_url():
        return reverse('blog_page')
