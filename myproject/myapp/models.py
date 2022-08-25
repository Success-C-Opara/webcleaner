from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    prize = models.IntegerField()
    sex = models.CharField(max_length=100)
    image=models.ImageField(blank=True,upload_to='image')

