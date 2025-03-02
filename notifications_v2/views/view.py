from rest_framework import generics, permissions, status
from rest_framework.response import Response

from notifications_v2.serializers.serializers import NotificationSerializer
from notifications_v2.services.notifications import NotificationService


class NotificationListCreateView(generics.ListCreateAPIView):
    """View for listing and creating notifications"""
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    service = NotificationService()

    def get_queryset(self):
        return self.service.find(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """Create a new notification"""
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if 'text' not in serializer.validated_data:
            return Response({"error": "The 'text' field is required."}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Corrected way to create a notification
        notification = self.service.create(user=request.user, text=serializer.validated_data['text'])

        return Response(NotificationSerializer(notification).data, status=status.HTTP_201_CREATED)


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a notification"""
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    service = NotificationService()
    lookup_field = 'pk'

    def get_queryset(self):
        return self.service.find(user=self.request.user)


    def delete(self, request, *args, **kwargs):
        """Delete a specific notification"""
        notification = self.service.find_by_id(kwargs.get('pk'))

        if not notification:
            return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)

        self.service.delete(notification.id)  # ✅ Ensure correct notification ID
        return Response({"success": True}, status=status.HTTP_200_OK)
