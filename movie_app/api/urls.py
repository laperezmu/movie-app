#Django imports
from django.urls import path, include

#Internal imports
from movie_app.api.views import (stream_platform_list, visual_content_list,
                                 stream_platform_details, visual_content_details)

#URLS

urlpatterns = [
    path('platform/', stream_platform_list, name='Stream-platform-list'),
    path('platform/<int:pk>', stream_platform_details, name='Stream-platform-details'),
    path('movies/', visual_content_list, name='Movies-list'),
    path('movies/<int:pk>', visual_content_details, name='Movie-details'),
]