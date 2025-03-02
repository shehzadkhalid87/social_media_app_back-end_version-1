from rest_framework import serializers
import re


class PasswordValidator():
    def __call__(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")

        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")

        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")

        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError("Password must contain at least one digit.")

        if not re.search(r"[!@#$%^&*()_+{};:.?|<>]", value):
            raise serializers.ValidationError("Password must contain at least one special character.")
