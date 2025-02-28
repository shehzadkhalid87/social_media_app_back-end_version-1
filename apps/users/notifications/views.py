from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import NotificationSerializer
from .models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationView(generics.ListAPIView, generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

    def update(self, request, *args, **kwargs):
        notification = self.get_object()  # Use get_object() to retrieve the notification
        if notification.recipient != request.user:
            return Response({"error": "You do not have permission to update this notification."}, status=status.HTTP_403_FORBIDDEN)
        notification.is_read = True
        notification.save()
        return Response(self.get_serializer(notification).data)