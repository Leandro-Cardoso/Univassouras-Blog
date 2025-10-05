from django.db import models
from django.contrib.auth.models import AbstractUser # <--- IMPORTANTE

class Role(models.Model):
    name = models.CharField(max_length = 100, unique = True, null = False)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class User(AbstractUser): 
    role = models.ForeignKey(
        'Role',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True, null = False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 100, unique = True, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.TextField(null = False)

    author = models.ForeignKey(
        'User',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    categories = models.ManyToManyField(
        'Category',
        blank = True
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length = 100, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.TextField(null = False)

    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return f"{self.author} - {self.post.title}"
