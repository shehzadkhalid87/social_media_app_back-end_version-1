from distutils.fancy_getopt import wrap_text

from PIL.ImageOps import equalize
from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.users.models import Profile
from serializers.passwordValidator import PasswordValidator
from serializers.emailValidator import EmailValidator

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[PasswordValidator()])
    email = serializers.CharField(write_only=True, validators=[EmailValidator()])
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data,password=8):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user) #Create a profile when a User is created.
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'profile_picture')