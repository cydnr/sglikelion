from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def front(request):
    return render(request, 'fan/front.html')


def home(request):
    posts = Post.objects.all
    return render(request, 'fan/home.html',{'posts_list':posts})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.writer = request.user
            post.save()
            return redirect('home')
            
    else:
        form = PostForm()
            
    return render(request, 'fan/new.html', {'form':form})

def post_detail(request, index):
    post = get_object_or_404(Post, pk=index)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment =  form.save(commit=False)
            comment.author = request.user
            comment.post=post
            comment.save()
            return redirect('post_detail', pk=index)
    elif request.method == "GET":
        form = CommentForm()
        comments = Comment.objects.filter(post=post)
        return render(request, "fan/post_detail.html", {'post':post, 'form':form, 'comments':comments})
 
def post_edit(request, index):
    post = get_object_or_404(Post, pk=index)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('post_detail',index=post.pk)
            
    else:
        form = PostForm(instance = post)
            
    return render(request, 'fan/post_edit.html', {'form':form})

def post_delete(request, index):
    post = get_object_or_404(Post, pk=index)
    post.delete()
    return redirect('home')