from django.conf import settings
from django.db import models
from django.utils.text import slugify

# Create your models here.

User = settings.AUTH_USER_MODEL


class MourseQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(slug__icontains=query) |
                Q(start_date__icontains=query) |
                Q(end_date__icontains=query)
                    )

        return self.filter(lookup)


class MourseManager(models.Manager):
    def get_queryset(self):
        return MourseQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Mourse(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(default='change-me', unique=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default="2021-12-25", null=True, blank=True)
    q_lectures = models.PositiveIntegerField()

    objects = MourseManager()

    class Meta:
        ordering = ['start_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Mourse, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/my_mourse/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
