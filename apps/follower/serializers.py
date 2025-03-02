from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.follower.models import Follower


User = get_user_model()

class FollowerSerializer(serializers.Serializer):
    follower_id = serializers.IntegerField(
        required=True,
        error_messages={"required": "Follower ID is required"}
    )
    following_id = serializers.IntegerField(
        required=True,
        error_messages={"required": "Following ID is required"}
    )
    def validate(self, data):
        """Ensure both users exist before creating a follower relationship"""
        follower_id = data.get("follower_id")
        following_id = data.get("following_id")
        if follower_id == following_id:
            raise serializers.ValidationError("A user cannot follow themselves.")

        return data
