from datetime import date

from django.conf import settings
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    # user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(default='change-me', unique=True)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    upload_date = models.DateField(default=date.today)

    class Meta:
        ordering = ['upload_date']
