from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from blog.models import Post
from blog.serializers import PostSerializer
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


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    Permission_class = [IsAuthenticatedOrReadOnly]
