from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from movie_app.models import StreamPlatform, VisualContent, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class VisualContentSerializer(serializers.ModelSerializer):
    platform = serializers.CharField(source = 'platform.name')

    class meta:
        model = VisualContent
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    visual_content = VisualContentSerializer(many = True, read_only = True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'