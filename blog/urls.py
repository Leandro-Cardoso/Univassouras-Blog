from django.urls import path
from .views import PostListView, PostCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("create", PostCreateView.as_view(), name = "create_post")
]
