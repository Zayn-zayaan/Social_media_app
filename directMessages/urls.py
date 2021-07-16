from django.urls import path
from .views import inbox, Directs, sendDirects, UserSearch, Newconvo

urlpatterns = [
    path('', inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('send/', sendDirects, name='send_direct'),
    path('new/', UserSearch, name='usersearch'),
    path('new/<username>', Newconvo, name='newconvo'),
    
]