import re
from django.contrib import admin
from movie_app.models import VisualContent, StreamPlatform, Review
# Register your models here.

admin.site.register(VisualContent)
admin.site.register(StreamPlatform)
admin.site.register(Review)