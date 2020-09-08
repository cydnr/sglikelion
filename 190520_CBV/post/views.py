from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class CreatePostView(CreateView):
    template_name = 'post/create.html'
    model = Post
    form_class = PostForm
    context_object_name = 'form'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePostView, self).form_valid(form)
        
class PostListView(ListView):
    template_name = 'post/list.html'
    model = Post
    ordering = '-timestamp'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'post/detail.html'
    model = Post
    context_object_name = 'post'
    
class PostUpdateView(UpdateView):
    template_name = 'post/create.html'
    model = Post
    form_class = PostForm
    context_object_name = 'form'
    success_url = '/'

class PostDeleteView(DeleteView):
    template_name = 'post/delete.html'
    model = Post
    context_object_name = 'form'
    success_url = '/'