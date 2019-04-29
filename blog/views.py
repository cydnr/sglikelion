from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.all
    return render(request, 'blog/home.html', {'posts':posts})
    

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/new.html', {'form': form})
    
def post_detail(request, index):
    post = get_object_or_404(Post, pk=index)
    return render(request, 'post_detail.html', {'post': post})
