from django.urls import path
from blog.views import *
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post', PostListView.as_view(), name='post-list'),
    path('post/<slug>', PostDetailView.as_view(), name='post-detail'),
    path('api/post-list', PostListAPIView.as_view(), name='post-api'),
]
