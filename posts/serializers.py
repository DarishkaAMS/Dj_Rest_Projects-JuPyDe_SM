from rest_framework import serializers

from .models import Post, PostLike


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'created_at', 'likes']


# class PostlikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostLike
#         fields = '__all__'
        
        
 
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'like_user', 'like_post', 'like', 'like_published'
        )


class PostDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = (
            'dislike_user', 'dislike_post', 'dislike', 'dislike_published'
        )
