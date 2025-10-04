from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "blog"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm() 
        return context

class PostCreateView(CreateView):
    model = Post
    fields = [
        "title",
        "category",
        "content"
    ]
    success_url = reverse_lazy("index")

class CategoryCreateView(CreateView):
    model = Category
    fields = [
        "name"
    ]
    success_url = reverse_lazy("create_post")

@require_POST
def create_comment(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit = False) 
        new_comment.post = post 
        new_comment.save()
        return redirect('index') 
    context = {
        'blog': Post.objects.all(),
        'comment_form': form
    }
    return render(request, 'blog/index.html', context)
