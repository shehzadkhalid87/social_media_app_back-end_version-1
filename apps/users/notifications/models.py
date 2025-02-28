from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# ... (CustomUser, Profile, Follower, Post, Comment, Like models remain the same)

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications', null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    notification_type = models.CharField(max_length=50) # like, comment, follow

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.message}"