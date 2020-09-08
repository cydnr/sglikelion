from django.conf.urls import url
from .views import CreatePostView, PostUpdateView, PostListView, PostDetailView 

urlpatterns = [
    url(r'^create/$', CreatePostView.as_view(), name='post-create'), 
    ]
