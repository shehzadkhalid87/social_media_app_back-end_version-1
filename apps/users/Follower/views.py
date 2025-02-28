from rest_framework import generics, permissions, status
from rest_framework.response import Response
from apps.users.Follower.serializers import FollowerSerializer
from apps.users.Follower.models import Follower
from django.contrib.auth import get_user_model

from apps.users.notifications.models import Notification

User = get_user_model()

class FollowerView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        follower = request.user
        following_id = serializer.validated_data['following'].id
        if follower.id == following_id:
            return Response({"error": "You can't follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Follower.objects.create(follower=follower, following=serializer.validated_data['following'])
            # Create notification
            Notification.objects.create(
                recipient=serializer.validated_data['following'],
                sender=follower,
                message=f"{follower.username} started following you.",
                notification_type="follow"
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        follower = request.user
        try:
            following_id = request.data['following']
        except KeyError:
            return Response({'error': 'The "following" field is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            follow_object = Follower.objects.get(follower=follower, following_id=following_id)
            follow_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Follower.DoesNotExist:
            return Response({'error': 'You are not following this user.'}, status=status.HTTP_404_NOT_FOUND)