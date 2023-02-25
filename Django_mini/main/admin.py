from django.contrib import admin
from .models import FoodRec

# Register your models here.
# admin.site.register(FoodRec)

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['context']

admin.site.register(FoodRec, QuestionAdmin)
