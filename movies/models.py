from django.db import models
from django.conf import settings
# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to="%Y/%m/$d/")
    title = models.CharField(max_length=100)
    description = models.TextField()
    GENRE_CHOICES = [
        ('comedy', 'Comedy'),
        ('romance', 'Romance'),
        ('fantasy', 'Fantasy'),
    ]
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    score = models.FloatField()


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
