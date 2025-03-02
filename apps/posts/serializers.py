from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.posts.models import Post, Comments, Likes


User = get_user_model()

# ... (UserSerializer, ProfileSerializer, FollowerSerializer remain the same)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'image', 'video', 'created_at', 'updated_at')
        read_only_fields = ('author', 'created_at', 'updated_at')


# comment serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'post', 'author', 'content', 'created_at')
        read_only_fields = ('author', 'created_at')


# Likes Serializer
class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ('id', 'post', 'user', 'created_at')
        read_only_fields = ('user', 'created_at')



