from django.urls import path
from django.urls import path, include, re_path

from . import views

app_name="main"

urlpatterns = [
    path('', views.PostHome.as_view(paginate_by=4), name="home"),
    path('food_detail/<int:pk>/',views.food_detail,name='food_detail'),
    path('about/',views.PostList.as_view(), name='about'),
    path('contact',views.contact, name='contact'),
    path('board_list',views.ListBoard.as_view(), name='post_list'),
    path('board_detail/<int:pk>/', views.board_detail,name='board_detail'),
    path('board_datail/<int:pk>/delete',views.board_delete,name='board_delete'),
    path('index/',views.ss,name='index'),
    


    path('<int:pk>/new_comment/', views.new_comment),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),



    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update')
    
    
]