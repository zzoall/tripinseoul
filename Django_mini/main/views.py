from django.shortcuts import render, get_object_or_404
from .models import FoodRec


# Create your views here.

def index(request):
    return render(request,'base/home.html')
    

def about(request):
    foodrec=FoodRec.objects.all()
    return render(request,'main/about.html',{'foodrec':foodrec})



def food_detail(request,pk):
    foodrec=get_object_or_404(FoodRec,pk=pk)
    return render(request,'main/food_detail.html',{'foodrec':foodrec})



def blog_home(request):
    return render(request,'main/blog-home.html')

def blog_post(request):
    return render(request,'main/blog-post.html')

def contact(request):
    return render(request,'main/contact.html')

def faq(request):
    return render(request,'main/faq.html')

def portfolio_item(request):
    return render(request,'main/portfolio-item.html')


def portfolio_overview(request):
    return render(request,'main/portfolio-overview.html')


