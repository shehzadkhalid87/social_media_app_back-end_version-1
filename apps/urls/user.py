from django.urls import path, include

from apps.follower.views import FollowerView
from apps.posts.views import PostView, PostDetailView
from apps.posts.views import FeedView, CommentView, LikesView

urlpatterns =[
path('posts/', include('apps.posts.urls')),
path('follow/', FollowerView.as_view(), name='follow'),
path('', PostView.as_view(), name='posts'),  # Change posts/ to ''
path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
path('feedback/', FeedView.as_view(), name='feed'),
path('comment/', CommentView.as_view(), name='comment'),
path('<int:pk>/comment/', CommentView.as_view(), name='comment'),
path("likes/", LikesView.as_view(), name="likes")

]