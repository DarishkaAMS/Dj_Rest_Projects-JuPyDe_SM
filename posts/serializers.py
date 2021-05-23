from rest_framework import serializers

from .models import Post, PostLike


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'created_at', 'likes']


class PostlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'