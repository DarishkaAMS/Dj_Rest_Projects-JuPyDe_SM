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


# LIKE_CHOICES = (
#     ('Like', 'Like'),
#     ('Unlike', 'Unlike'),
# )


# class PostLike(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     value = models.CharField(choices=LIKE_CHOICES, max_length=8)

#     def __str__(self):
#         return f"{self.user}-{self.post}-{self.value}"


class PostLike(models.Model):
    like_user = models.ForeignKey(User, related_name='like_user', on_delete=models.CASCADE)
    like_post = models.ForeignKey(Post, related_name='like_post', on_delete=models.CASCADE)
    like = models.SmallIntegerField(default=0)
    like_published = models.DateField(format('%Y-%m-%d'), auto_now_add=True)


class PostDislike(models.Model):
    dislike_user = models.ForeignKey(User, related_name='dislike_user', on_delete=models.CASCADE)
    dislike_post = models.ForeignKey(Post, related_name='dislike_post', on_delete=models.CASCADE)
    dislike = models.SmallIntegerField(default=0)
    dislike_published = models.DateField(format('%Y-%m-%d'), auto_now_add=True)




