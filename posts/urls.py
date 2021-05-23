from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListAPIView.as_view(), name="posts"),
    path('<int:id>', views.PostDetailAPIView.as_view(), name="post"),
]
