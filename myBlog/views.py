# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# List all posts or create a new post
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Retrieve, update, or delete a single post
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#login
def login_view(request):
    return render(request, 'login.html')

#page for creating the posts
@login_required
def blog_view(request):
    return render(request, 'myblogs.html')
