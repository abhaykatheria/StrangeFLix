from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Movie(models.Model):  
    name = models.CharField(max_length=30)  
    genre = models.CharField(max_length=30)
    file = models.FileField()
    thumbnail = models.FileField()
    views = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('screens:movie_detail', args=[str(self.id)])

