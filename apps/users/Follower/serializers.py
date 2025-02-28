from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.users.Follower.models import Follower

User = get_user_model()

# ... (UserSerializer and ProfileSerializer remain the same)

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id', 'follower', 'following')
        unique_together = ('follower', 'following')