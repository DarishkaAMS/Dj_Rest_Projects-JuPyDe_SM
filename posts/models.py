from datetime import date

from django.conf import settings
from django.db import models
from django.utils.text import slugify
from users.models import User

# Create your models here.


class PostQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(slug__icontains=query) |
                Q(start_date__icontains=query) |
                Q(end_date__icontains=query)
                    )

        return self.filter(lookup)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Post(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(default='change-me', unique=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    upload_date = models.DateField(default=date.today)

    objects = PostManager()

    class Meta:
        ordering = ['upload_date']
