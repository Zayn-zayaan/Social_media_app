from django.db import models
from django.db.models import signals
from post.models import Post
from notifications.models import Notifications
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def user_comment_notify(instance, sender, *args, **kwargs):
        comment = instance
        post = comment.post
        text_preview = comment.body[:90]
        sender = comment.user
        if sender != post.user:
            notify = Notifications(post=post, sender=sender, user=post.user, text_preview=text_preview, notification_type=2)
            notify.save()

    def user_del_comment_notify(instance, sender, *args, **kwargs):
        comment = instance
        post = comment.post
        text_preview = comment.body[:90]
        sender = comment.user
        notify = Notifications.objects.filter(post=post, sender=sender, user=post.user, notification_type=2)
        notify.delete()

# Comment Notifications signals
post_save.connect(Comment.user_comment_notify, sender=Comment)
post_delete.connect(Comment.user_del_comment_notify, sender=Comment)