from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    quality = models.CharField(max_length=50)
    voice = models.CharField(max_length=100)
    duration = models.PositiveSmallIntegerField()
    description = models.TextField()
    picture = models.TextField()
    file = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.pk})

    def get_genres_split(self):
        return self.genre.split('/')

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
