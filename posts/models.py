from django.db import models
from authentication.models import User


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_user', blank=True, through='PostLike')

    class Meta:
        ordering: ['-created_at']

    def __str__(self):
        return str(self.title)


class PostLike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
