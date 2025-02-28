from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.users.serializers.serializers import UserSerializer, ProfileSerializer
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class TokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

class TokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']