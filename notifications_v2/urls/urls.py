from django.urls import path
from notifications_v2.views.view import NotificationListCreateView,NotificationDetailView

urlpatterns = [
    path('', NotificationListCreateView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),

]
