from django.contrib import admin
from blog.models import Post, Category, Comment
from blog.actions import *
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'author', 'category', 'is_deleted']
    list_per_page = 8
    ordering = ['title', 'author', 'content']
    search_fields = ['title', 'author__username']
    list_display = ['title', 'category', 'author', 'is_deleted']
    list_filter = ['is_deleted']
    actions = [set_title_test]
    set_title_test.short_description = 'Set Title'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('name', 'content')
