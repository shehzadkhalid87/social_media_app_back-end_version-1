from notifications_v2.repository.notification import NotificationRepository


class NotificationService:
    _repo = NotificationRepository()

    def create(self, user, text):
        """Create a notification."""
        return self._repo.create(user=user, text=text)  # ✅ Use named arguments

    def find(self, **kwargs):
        """Find a notification."""
        return self._repo.find(**kwargs)

    def find_all(self, **kwargs):
        """Find all notifications."""
        return self._repo.find(**kwargs)

    def find_by_id(self, id):
        """Find a notification by ID."""
        return self._repo.find_by_id(id)

    def find_by_user(self, user):
        """Find notifications by user."""
        return self._repo.find(user=user)

    def find_all_by_user(self, user):
        """Find all notifications by user."""
        return self._repo.find(user=user)

    def delete(self, id):
        """Delete a notification by ID."""
        return self._repo.delete(id)
