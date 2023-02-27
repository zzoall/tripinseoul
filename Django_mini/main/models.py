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


class Category(models.Model):
    categoryName = models.CharField(max_length=30, unique=True) 
    slug = models.SlugField(max_length=30, unique=True, allow_unicode=True)

    def __str__(self):
        return self.categoryName



    class Meta:
        verbose_name_plural = 'categories'
    
class Board(models.Model) :
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) 
    title=models.CharField(max_length=30)
    context=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    likes = models.ManyToManyField(User, related_name='like_posts')

    
    def __str__(self):
        return f'[[{self.pk}] {self.title}            by {self.author}]'
    
    
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    updated_at = models.DateTimeField(auto_now=True)  # 값을 변경할 수 있음. default 값으로 현재시간이 찍혀있음 
    post = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.author} / {self.content}]'



    
    
    
    