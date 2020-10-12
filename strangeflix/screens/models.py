from django.db import models

# Create your models here.
class Movie(models.Model):  
    name = models.CharField(max_length=30)  
    genre = models.CharField(max_length=30)
    file = models.FileField()
    thumbnail = models.FileField()
    views = models.IntegerField()

    def _str_(self):
        return self.name

