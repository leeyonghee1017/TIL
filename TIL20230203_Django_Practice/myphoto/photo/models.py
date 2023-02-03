from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=50)
    autho = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    decription = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.title)