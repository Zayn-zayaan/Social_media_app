from celery import shared_task
from stories.models import Story, StoryStream
from datetime import datetime, timedelta

@shared_task
def CheckStoriesDate():
    exp_date = datetime.now() - timedelta(hours=1)
    old_stories = Story.objects.filter(posted__lt=exp_date)
    old_stories.update(expired=True)
    print("Stories updateddddd")

@shared_task
def DeleteExpired():
    Story.objects.filter(expired=True).delete()
    StoryStream.objects.filter(story=None).delete()