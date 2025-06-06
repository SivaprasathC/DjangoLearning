from django.db import models

# Create your models here.
class Destination(models.Model):
    #refer Django documentation for model fields #id is given by default
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    descp = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)  
