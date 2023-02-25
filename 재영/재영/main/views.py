from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import FoodRec
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

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

@csrf_exempt
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password"]:
            user = User.objects.create_user( 
                username=request.POST["username"], 
                email=request.POST["email"], 
                password=request.POST["password"]) 
            auth.login(request,user)
            return redirect("login")
        return render(request,"base/sigup.html")

    return render(request, 'base/signup.html')
            
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'base/Login.html', {'error': '비번 틀림'})
    else:        
        return render(request,'base/Login.html')

def logout(request):
    auth.logout(request)
    return redirect("login")