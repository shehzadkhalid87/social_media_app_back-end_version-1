from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
class NotificationEntity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notification_entity"

    def __str__(self):
        return f"Notification for {self.user.username} : {self.text}[:50]"