from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# 세현님 작성
class FoodRec(models.Model):
    region= models.CharField(max_length=10)
    gu=models.CharField(max_length=10)
    dong=models.CharField(max_length=10)
    title=models.CharField(max_length=20)
    image=models.CharField(max_length=200)
    context=models.TextField()


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    crate_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()