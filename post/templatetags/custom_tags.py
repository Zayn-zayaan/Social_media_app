from django import template
from authy.models import Profile
from post.models import Likes

register = template.Library()

@register.filter(name='favorited')
def favorited(post_id, user_id):
    profile = Profile.objects.get(user=user_id)
    if profile.favorites.filter(id=post_id).exists():
            return True
    else:
        return False

@register.filter(name='liked')
def liked(post_id, user_id):
    if Likes.objects.filter(user=user_id, post=post_id).exists():
            return True
    else:
            return False

# @register.filter
# def lower(value):
#     return value.lower()
