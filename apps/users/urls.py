from django.urls import path


from .views import UserCreateView, ProfileDetailView, TokenObtainPairView, TokenRefreshView, UserSearchView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('Login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),


]