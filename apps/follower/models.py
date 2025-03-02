from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # app_label = 'Follower'
        unique_together = ('follower', 'following')
        # changing table name in database
        db_table = "follower"

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"