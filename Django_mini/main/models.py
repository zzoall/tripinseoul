from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class FoodRec(models.Model):
    region= models.CharField(max_length=10)
    gu=models.CharField(max_length=10)
    dong=models.CharField(max_length=10)
    title=models.CharField(max_length=30)
    context=models.TextField()
    header_img = models.ImageField(upload_to='main/images/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'[[{self.pk}] {self.title}            by {self.author}]'


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