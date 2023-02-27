from django import forms 
from django.db import models
from django.contrib.auth.models import User
from .models import Comment,FoodRec,Category,Board
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class PostForm(forms.ModelForm):
    
    class Meta:
        model = FoodRec
        fields = ("region",)
        
class CommentForm(forms.ModelForm): 
    
  
    class Meta:
        model = Comment
        fields = ('content', )
        
        
class CustomUserChangeForm(UserChangeForm) :
    
    class Meta :
        # model = User
        model = get_user_model()
        fields = ('email', 'password')

class PostForm(forms.ModelForm):
    
    class Meta:
        model = FoodRec
        fields = ("region",)