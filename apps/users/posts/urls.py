from django.urls import path
from .views import PostView, PostDetailView, CommentView, LikesView
from .views import FeedView

urlpatterns = [
    path('', PostView.as_view(), name='posts'), #Change posts/ to ''
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('feedback/', FeedView.as_view(), name='feed'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('<int:pk>/comment/', CommentView.as_view(), name='comment'),
    path("likes/", LikesView.as_view(), name="likes")
]