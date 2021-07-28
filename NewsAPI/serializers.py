# serializers.py

from rest_framework import serializers

from scraping.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('description', 'guid', 'link', 'pubDate', 'title')