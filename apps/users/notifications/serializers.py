from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.users.Follower.models import Follower
from apps.users.notifications.models import Notification

User = get_user_model()

# ... (UserSerializer, ProfileSerializer, FollowerSerializer, PostSerializer, CommentSerializer, LikeSerializer remain the same)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'recipient', 'sender', 'message', 'is_read', 'created_at', 'notification_type')
        read_only_fields = ('recipient', 'sender', 'created_at')