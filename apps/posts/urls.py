from django.urls import path
from apps.posts.views import PostView, PostDetailView, CommentView

urlpatterns = [
    path('', PostView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_pk>/comments/', CommentView.as_view(), name='post-comments'),
    path('comments/<int:pk>/', CommentView.as_view(), name='comment-detail'),
]