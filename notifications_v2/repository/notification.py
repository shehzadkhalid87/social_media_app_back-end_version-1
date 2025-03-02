from notifications_v2.models.notification import NotificationEntity


class NotificationRepository:
    _object = NotificationEntity

    def create(self, **kwargs):
        """Create a new notification using named arguments"""
        return self._object.objects.create(**kwargs)  # ✅ Use **kwargs only, remove *args

    def find(self, **kwargs):
        return self._object.objects.filter(**kwargs)

    def find_by_id(self, id):
        return self._object.objects.filter(id=id).first()

    def update(self, id, **kwargs):
        """Update a notification by notification ID"""
        notification = self.find_by_id(id)
        if notification:
            for key, value in kwargs.items():
                setattr(notification, key, value)
            notification.save()
            return notification
        return None

    def delete(self, id):
        """Delete a notification by notification ID"""
        notification = self.find_by_id(id)
        if notification:
            notification.delete()
            return True
        return False
