from django.urls import path
from .views import  FollowerView

urlpatterns = [
    # ... (other URLs)
    path('follow/', FollowerView.as_view(), name='follow'),
]