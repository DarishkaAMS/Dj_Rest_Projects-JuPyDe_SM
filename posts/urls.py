from django.urls import path
from .views import PostDetailAPIView, PostListAPIView


urlpatterns = [
    path('', PostListAPIView.as_view(), name="posts"),
    path('<int:id>', PostDetailAPIView.as_view(), name="post"),
    # path('like/<int:id>', like_view, name="like_post"),
]
