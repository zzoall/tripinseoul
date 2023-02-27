from django.contrib import admin
from .models import FoodRec,Comment,Category,Board

# Register your models here.
# admin.site.register(FoodRec)

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['context']

admin.site.register(FoodRec, QuestionAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Board)

