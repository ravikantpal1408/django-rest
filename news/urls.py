from django.urls import path
from news.views import article_list_create_api_view

urlpatterns = [
    path('v1/articles/', article_list_create_api_view, name='article-list')
]
