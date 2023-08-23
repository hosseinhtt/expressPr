from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post
# Create your views here.


class IndexView(TemplateView):
    template_name = 'blog/index.html'
    person = {'name': 'Hossein', 'lastname': 'htt', 'age': 29}
    extra_context = person


class PostListView(ListView):
    queryset = Post.objects.filter()
    template_name = 'blog/post.html'
    context_object_name = 'post'


class PostDetailView(DetailView):
    queryset = Post.objects.filter()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
