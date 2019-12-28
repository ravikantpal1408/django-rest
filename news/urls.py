from django.urls import path
# from news.views import article_list_create_api_view, article_detail_api_view
from news.views import ArticleListCreateAPIView, ArticleDetailAPIView

#   now implementing the class based view url scheme

urlpatterns = [
    path('v1/articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('v1/articles/<int:pk>',
         ArticleDetailAPIView.as_view(), name='article-detail'),
    # path('v1/articles/', article_list_create_api_view, name='article-list'),
    # path('v1/articles/<int:pk>', article_detail_api_view, name='article-detail'),
]
