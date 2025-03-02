from django.utils.timezone import now

from notifications_v2.services.notifications import NotificationService

notifications_service = NotificationService()

def create_notification(user, text):
    """Helper function to create a new notification."""
    return notifications_service.create(user, text)


def format_notification(username, action):
    """Helper function to format a notification."""
    return f"{username} {action} at {now().strftime('%Y-%m-%d %H:%M:%S')}"

def get_user_notifications(user):
    """Retrives notifications for a user."""
    return notifications_service.find(user=user)