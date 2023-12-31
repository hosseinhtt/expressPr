from django.urls import path
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views

from blog.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post', PostListView.as_view(), name='post-list1'),
    path('post/<slug>', PostDetailView.as_view(), name='post-detail'),
    path('api/post-list', PostListAPIView.as_view(), name='post-api'),
    # path('api-token-auth/', views.obtain_auth_token),

]

router = DefaultRouter()
router.register(r'api/post', PostViewSet)
urlpatterns += router.urls
