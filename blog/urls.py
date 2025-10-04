from django.urls import path
from .views import PostListView, PostCreateView, CategoryCreateView, create_comment

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("create", PostCreateView.as_view(), name = "create_post"),
    path("category", CategoryCreateView.as_view(), name = "create_category"),
    path('post/<int:post_pk>/comment/new/', create_comment, name='create_comment'), 
]
