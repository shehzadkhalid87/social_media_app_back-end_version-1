from rest_framework import serializers
from notifications_v2.models.notification import NotificationEntity


class NotificationSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)  # Ensure 'text' is required

    class Meta:
        model = NotificationEntity
        fields = ['id', 'user', 'text', 'created_at']
