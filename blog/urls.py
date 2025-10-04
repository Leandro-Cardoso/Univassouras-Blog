from django.urls import path
from .views import PostListView, PostCreateView, CategoryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("create", PostCreateView.as_view(), name = "create_post"),
    path("category", CategoryCreateView.as_view(), name = "create_category")
]
