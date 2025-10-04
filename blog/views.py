from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "blog"

class PostCreateView(CreateView):
    model = Post
    fields = [
        "title",
        "category",
        "content"
    ]
    success_url = reverse_lazy("index")
