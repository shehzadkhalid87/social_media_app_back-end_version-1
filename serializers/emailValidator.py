from rest_framework import serializers
import re

class EmailValidator:
    def __call__(self, value):
        if not value:
            raise serializers.ValidationError("Email address cannot be empty. Email is required.")


        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.search(pattern, value):
            raise serializers.ValidationError("Invalid email address.")

        return value




