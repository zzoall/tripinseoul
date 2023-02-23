from django.db import models

# Create your models here.
class FoodRec(models.Model):
    region= models.CharField(max_length=10)
    gu=models.CharField(max_length=10)
    dong=models.CharField(max_length=10)
    title=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    image=models.CharField(max_length=200)
    context=models.TextField()