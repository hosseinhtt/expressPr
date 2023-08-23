from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def get_deleted(self):
        return super().get_queryset().filter(is_deleted=True)

    def get_all(self):
        return super().get_queryset()


class BaseModel(models.Model):
    objects = BaseManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'


class Post(BaseModel):
    title = models.CharField(
        max_length=50, help_text='Enter the title', default='post-number')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.author}: {self.title=}- {self.content[:15]}'


class Comment(BaseModel):
    name = models.CharField(max_length=20)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.content[:10]}...'
