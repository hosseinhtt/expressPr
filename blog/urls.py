from django.urls import path
from rest_framework.routers import DefaultRouter

from blog.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post', PostListView.as_view(), name='post-list'),
    path('post/<slug>', PostDetailView.as_view(), name='post-detail'),
    path('api/post-list', PostListAPIView.as_view(), name='post-api'),
]

router = DefaultRouter()
router.register(r'api/post', PostViewSet)
urlpatterns += router.urls
