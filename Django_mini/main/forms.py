from django import forms 
from django.db import models
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("region", "gu", "dong", "title", "context", "header_img")