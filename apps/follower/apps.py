from django.apps import AppConfig


class FollowerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.follower"
    label = "follower_app"  # Ensure a unique label
