from rest_framework import generics, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, LikesSerializer
from .models import  Post,Likes
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

from ..follower.models import Follower

User = get_user_model()
 # custom page size for post Views
class CustomPagination(PageNumberPagination):
    page_size = 5

# ... (UserCreateView, ProfileDetailView, TokenObtainPairView, TokenRefreshView, FollowerView remain the same)

class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination,
    filter_backends = [DjangoFilterBackend]
    filterer_fields = ['content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ... (UserCreateView, ProfileDetailView, TokenObtainPairView, TokenRefreshView, FollowerView, PostView remain the same)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination


    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response({"error": "You don't have permission to delete this post."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response({"error": "You don't have permission to update this post."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

class FeedView(generics.ListAPIView):
      serializer_class = PostSerializer
      permission_classes = [permissions.IsAuthenticated]
      pagination_class = CustomPagination

      def get_queryset(self):
        user = self.request.user
        following = Follower.objects.filter(follower=user).values_list('following', flat=True)
        return Post.objects.filter(author__in=following).order_by('-created_at')

# CommentView
class CommentView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def destroy(self, request, *args, **kwargs):
        comments = self.get_object()
        if comments.author != request.user:
            return Response({"error": "You don't have permission to delete this comment."}, status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)


# likes view
class LikesView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            likes = Likes.objects.get(post=request.data['post'], user=request.user)
            likes.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Likes.DoesNotExist:
            return Response({"error": "Likes does not exist."}, status=status.HTTP_404_NOT_FOUND)

