from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from authentication.models import User
from .models import Post, PostLike
from .serializers import PostSerializer
# Create your views here.


class PostListAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        user = User.objects.get(user=user)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = PostLike.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

            post_obj.save()
            like.save()

