from django.urls import path
from .views import NewStory, ShowMedia

urlpatterns = [
    path('newstory/', NewStory, name='newStory'),
    path('showMedia/<stream_id>', ShowMedia, name='showMedia'),
]
