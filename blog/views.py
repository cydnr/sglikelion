from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect ('post-list')
    elif request.method == "GET":
        form = PostForm()
        return render(request, "blog/create.html", {'form':form})

@login_required        
def view_post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/list.html", {'posts':posts})

@login_required
def view_post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment =  form.save(commit=False)
            comment.author = request.user
            comment.post=post
            comment.save()
            return redirect('post-detail', pk=pk)
    elif request.method == "GET":
        form = CommentForm()
        comments = Comment.objects.filter(post=post)
        return render(request, "blog/detail.html", {'post':post, 'form':form, 'comments':comments})
        
        