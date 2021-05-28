from django.urls import path
from .views import PostDetailAPIView, PostListAPIView, like_unlike_post, PostAnaliticsLikesView, PostDislikeView, PostLikeView


urlpatterns = [
    path('', PostListAPIView.as_view(), name="posts"),
    path('<int:id>', PostDetailAPIView.as_view(), name="post"),
#     path('posts_like/<int:id>', like_unlike_post, name='like-post-view'),
    path('post/<int:post_pk>/<int:user_pk>/like/', PostLikeView.as_view(), name='post_like'),
    path('post/<int:post_pk>/<int:user_pk>/dislike/', PostDislikeView.as_view(), name='post_dislike'),
    path('posts_like/analitics/date_from=<date_from>&date_to=<date_to>/', PostAnaliticsLikesView.as_view(), name='post_likes'),

]
