from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, CategoryListView, CategoryCreateView, CategoryDeleteView, create_comment

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("create", PostCreateView.as_view(), name = "create_post"),
    path("post/<int:pk>/edit", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("category", CategoryCreateView.as_view(), name = "create_category"),
    path('post/<int:post_pk>/comment/new/', create_comment, name='create_comment'),
    path("categories", CategoryListView.as_view(), name="categories"),
    path("category/<int:pk>/delete", CategoryDeleteView.as_view(), name="category_delete"),
]

# TODO: List categories
# TODO: Delete category
