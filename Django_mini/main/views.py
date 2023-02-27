from django.shortcuts import render, get_object_or_404
from .models import FoodRec
from django.views.generic import ListView


# Create your views here.
class PostHome(ListView):
    model = FoodRec
    ordering = '-pk'
    template_name = 'base/home.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostHome, self).get_context_data(**kwargs)
        context['first_post'] = FoodRec.objects.all().last()
        return context

class PostList(ListView):
    model = FoodRec
    ordering = '-pk'
    template_name = 'main/about.html'
    context_object_name = 'posts'
    paginate_by = 4
    paginate_orphans = 2

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['first_post'] = FoodRec.objects.all().last()
        return context


# def about(request):
#     foodrec=FoodRec.objects.all()
#     return render(request,'main/about.html',{'foodrec':foodrec})



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

