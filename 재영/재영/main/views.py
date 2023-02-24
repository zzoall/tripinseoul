from django.shortcuts import render ,get_object_or_404
from django.contrib.auth import authenticate
from .models import FoodRec

# Create your views here.

def index(requset):
    
    return render(requset,'base/home.html')
    

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


def pricing(request):
    return render(request,'main/pricing.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
        else:
            print("인증실패")
    return render(request,'base/Login.html')