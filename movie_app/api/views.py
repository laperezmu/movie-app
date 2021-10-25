from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *

from movie_app.models import StreamPlatform, Review, VisualContent
from movie_app.api.serializers import StreamPlatformSerializer, ReviewSerializer, VisualContentSerializer


@api_view(['GET'])
def stream_platform_list(request):
    queryset = StreamPlatform.objects.all()
    serializers = StreamPlatformSerializer(queryset, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def stream_platform_details(request, pk):
    queryset = StreamPlatform.objects.get(id = pk)
    serializers = StreamPlatformSerializer(queryset)
    return Response(serializers.data)


@api_view(['GET'])
def visual_content_list(request):
    queryset = VisualContent.objects.all()
    serializers = VisualContentSerializer(queryset, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def visual_content_details(request, pk):
    queryset = VisualContent.objects.get(id = pk)
    serializers = VisualContentSerializer(queryset)
    return Response(serializers.data)