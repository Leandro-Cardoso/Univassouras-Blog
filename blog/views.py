from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.core.exceptions import ImproperlyConfigured
from .models import Post, Category
from .forms import CommentForm

class RoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    required_role = None
    def __init__(self, *args, **kwargs):
        if self.required_role is None:
            raise ImproperlyConfigured(
                "RoleRequiredMixin requires 'required_role' to be defined."
            )
        super().__init__(*args, **kwargs)
    def test_func(self):
        user = self.request.user
        if not hasattr(user, 'role') or not user.role:
            return False
        return user.role.name.lower() == self.required_role.lower()
    def handle_no_permission(self):
        return redirect('index')
    
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
    required_role = "admin"
    fields = [
        "title",
        "category",
        "content"
    ]
    success_url = reverse_lazy("index")
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostUpdateView(RoleRequiredMixin, UpdateView):
    model = Post
    required_role = "admin"
    fields = [
        "title",
        "category",
        "content"
    ] 
    template_name = 'blog/post_update.html'
    context_object_name = 'post'
    success_url = reverse_lazy('index')

class CategoryCreateView(CreateView):
    model = Category
    required_role = "admin"
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
