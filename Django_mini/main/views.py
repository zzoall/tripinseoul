from django.shortcuts import render, get_object_or_404,redirect
from .models import FoodRec,Board,Comment
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm, CustomUserChangeForm
from django.views.decorators.http import require_POST
from django.contrib.auth import logout as auth_logout 
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied # 인가 - 권한이 있는 경우가 아니면 발생시키는 예외처리


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
    ordering = 'pk'
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

class ListBoard(ListView):
    model=Board
    ordering='pk'
    template_name='main/board_list.html'
    context_object_name = 'boards'
    paginate_by = 5
    paginate_orphans = 2
    
    def get_context_data(self, **kwargs):
        context = super(ListBoard, self).get_context_data(**kwargs)
        context['first_post'] = Board.objects.all().last()
        return context
    
def board_detail(request, pk):
    board =get_object_or_404(Board,pk=pk)
    return render(request, 'main/board_detail.html', {'board': board})


def board_delete(request,pk):
    login_session=request.session.get('login_session','')
    board=get_object_or_404(Board,pk=pk)
    if board.author==login_session:
        board.delete()
        return redirect('/board_list')
    else: 
        return redirect(f'/board_detail/{pk}')
    
class BoardCreate(CreateView):
    model= Board
    fields = ['category','title','context','author']
    success_url='/'
    template_name='create.html'
    
    def form_valid(self, form):
        model = form.save(commit=False)
      
        model.save()
        return super().form_valid(form)





class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def food_detail(request,pk):
    foodrec=get_object_or_404(FoodRec,pk=pk)
    return render(request,'main/food_detail.html',{'foodrec':foodrec})




def contact(request):
    return render(request,'main/contact.html')

def faq(request):
    return render(request,'main/faq.html')


def ss(request) :
    return render(request,'main/index.html')



def new_comment(request, pk):
    # 일단 로그인상태인지 확인을 합니다
    if request.user.is_authenticated:
        # 없는 글을 호출한 경우 -> 404 에러를 내거나
        post = get_object_or_404(Post, pk=pk)
        # 있으면 post를 전달하되 글번호에 맞는 post를 전달합니다. 
        # post = Post.objects.filter(pk=pk)
    # 그리고 데이터가 잘 왔는지 확인합니다 
        if request.method=='POST':
            comment_form = CommentForm(request.POST)
            # comment_form이 인가를 거친 폼이면(아무가 아니라 로그인하고 댓글 쓸 자격이 있는 사람의 코멘트이면)
            if comment_form.is_valid():
            # 그리고 데이터를 DB에 넣어줍니다
                comment = comment_form.save(commit=False) # commit
                comment.post = post
                comment.author = request.user
                comment.save()
            # blog/post_list.html, 글번호가 있는 자리 -> 이 자리를 어딘가에서 만들어주면 될 거 같아요
            # 새로 바뀐 DB(등록된 댓글)의 데이터를 가지고 화면으로 돌아갑니다 
                return redirect(comment.get_absolute_url())
            else:
                return redirect(post.get_absolute_url())
        else:
            raise PermissionDenied

    
class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk) # 댓글을 달 포스트를 가져오거나 404 에러를 발생합니다.
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete() # delete() 요청시 바로 삭제되도록 (즉시로딩) 구현되어있습니다
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied






@require_POST # POST 접근
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request) 
        # session 지우기. -> 아니면 이미 로그인 되어있는 상태로 남아있어서 탈퇴된 회원이 여기저기 글을 쓰거나, 지우거나, 악플도 달 수 있음 
        # 단 탈퇴후 로그아웃순으로 처리. 
        # 먼저 로그아웃하면 해당 request 객체 정보(쿠키)가 없어져서 삭제가 안됨.
        return redirect('')
    
    
@require_POST 
def logout(request):
    auth_logout(request)  # 자체적으로 제공하는 기능 사용 
    return redirect('')  
 
@login_required
def update(request) :
    if request.method == "POST" :
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid() :
            form.save()
            return redirect('')
    else :
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, '', context)