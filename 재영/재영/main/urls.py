from django.urls import path, include

from . import views

app_name="main"
urlpatterns = [
    path('', views.index, name='index'),
    
    
    path('food_detail/<int:pk>/',views.food_detail,name='food_detail'),
    
    
    
    path('about',views.about, name='about'),
    path('blog-home',views.blog_home, name='blog-home'),
    path('blog-post',views.blog_post, name='blog-post'),
    path('contact',views.contact, name='contact'),
    path('faq',views.faq, name='faq'),
    path('portfolio-item',views.portfolio_item, name='portfolio-item'),
    path('portfolio-overview',views.portfolio_overview, name='portfolio-overview'),
    path('pricing',views.pricing, name='pricing'),
    path('accounts/', include('accounts.urls')),
    path('login', views.login_view, name='login') 
    
    
]