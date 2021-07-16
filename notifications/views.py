from django.shortcuts import redirect, render
from .models import Notifications

# Create your views here.

def ShowNotifications(request):
    user = request.user
    notifications = Notifications.objects.filter(user=user).order_by('-date')
    Notifications.objects.filter(user=user, is_seen=False).update(is_seen=True)
    context = {
        'notifications': notifications,
    }

    return render(request, 'notifications.html', context)

def DeleteNotifications(request, not_id):
    user = request.user
    Notifications.objects.filter(id=not_id, user=user).delete()
    return redirect('show-notifications')

def CountNotifications(request):
    count_notifications = 0
    if request.user.is_authenticated:
        count_notifications = Notifications.objects.filter(user=request.user, is_seen=False).count()

    return {'count_notifications': count_notifications}