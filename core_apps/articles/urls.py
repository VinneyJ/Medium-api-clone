from django.urls import path
from .views import (
    ArticleListAPIView,
    ArticleCreateAPIView,
    ArticleDetailView,
    ArticleDeleteAPIView,
    update_article_api_view,
)


urlpatterns = [
    path("all/", ArticleListAPIView.as_view(), name="all-articles"),
    path("create/", ArticleCreateAPIView.as_view(), name="create-article"),
    path("detail/<slug:slug>/", ArticleDetailView.as_view(), name="article-detail"),
    path("delete/<slug:slug>/", ArticleDeleteAPIView.as_view(), name="article-delete"),
    path("update/<slug:slug>/", update_article_api_view, name="article-update"),
]