from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import NewsSerializer
from .pagination import StandardResultsSetPagination
from scraping.models import News

# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    # Fetching data from DB
    queryset = News.objects.all().order_by('-pubDate')
    serializer_class = NewsSerializer
    pagination_class = StandardResultsSetPagination