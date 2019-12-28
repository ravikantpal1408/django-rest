# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# calling models
from news.models import Article
from news.api.serializers import ArticleSerializers


# Create your views here.
@api_view(["GET"])
def article_list_create_api_view(request):
    if request.method == "GET":
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)
