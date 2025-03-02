from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from apps.follower.models import Follower
from apps.follower.serializers import FollowerSerializer
from notifications_v2.models.notification import NotificationEntity

User = get_user_model()

class FollowerView(generics.CreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        following_id = serializer.validated_data['following_id']
        follower_id = serializer.validated_data['follower_id']

        follower = User.objects.filter(id=following_id).first()
        if not follower:
            return Response({"error": f"User with id {following_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        following = User.objects.filter(id=follower_id).first()
        if not following:
            return Response({"error": f"User with id {follower_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if Follower.objects.filter(follower=follower, following=following).exists():
            return Response({"error": "You are already following this user"}, status=status.HTTP_400_BAD_REQUEST)

        #Create follower relationship
        Follower.objects.create(follower=follower, following=following)
        # Create notification
        NotificationEntity.objects.create(
            recipient=following,
            sender=follower,
            message=f"{follower.username} started following you.",
            notification_type="follow"
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

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