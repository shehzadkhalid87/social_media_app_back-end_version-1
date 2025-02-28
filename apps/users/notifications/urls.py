from django.urls import path
from .views import NotificationView

urlpatterns = [
    # ... (other URLs)
    path('', NotificationView.as_view(), name='notifications'),
    path('<int:pk>/', NotificationView.as_view(), name='notification-detail'),
]