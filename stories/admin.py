from django.contrib import admin
from .models import Story, StoryStream

# Register your models here.
admin.site.register(StoryStream)
admin.site.register(Story)

