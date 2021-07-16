from django.urls import path
from notifications.views import ShowNotifications, DeleteNotifications

urlpatterns = [
    path('', ShowNotifications, name='show-notifications'),
    path('<not_id>/delete', DeleteNotifications, name='delete-notifications'),
]
