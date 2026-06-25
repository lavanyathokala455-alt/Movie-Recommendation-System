from django.db import models

# Create your models here
class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()

    actor = models.CharField(max_length=200, default="N/A")
    director = models.CharField(max_length=200, default="N/A")
    description = models.TextField(default="N/A")
    language=models.CharField(max_length=50, default="English")
    poster = models.ImageField(upload_to='posters/', default='')
    trailer_url=models.URLField(max_length=200,blank=True, null=True)

