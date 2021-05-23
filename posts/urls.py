from django.urls import path
from .views import PostDetailAPIView, PostListAPIView, like_unlike_post


urlpatterns = [
    path('', PostListAPIView.as_view(), name="posts"),
    path('<int:id>', PostDetailAPIView.as_view(), name="post"),
    path('posts_like/<int:id>', like_unlike_post, name='like-post-view'),
]
