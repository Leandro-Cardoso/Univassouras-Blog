from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length = 100, unique = True, null = False)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class User(models.Model):
    DEFAULT_ROLE_ID = 1

    username = models.CharField(max_length = 100, unique = True, null = False)
    password = models.CharField(max_length = 100, null = False)
    created_at = models.DateTimeField(auto_now_add = True)

    role = models.ForeignKey(
        'Role',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        default = DEFAULT_ROLE_ID
    )

    def __str__(self):
        return self.username
