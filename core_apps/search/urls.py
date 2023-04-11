from django.urls import path
from rest_framework import routers
from .views import ArticleSearchView

routers = routers.DefaultRouter()
routers.register('search', ArticleSearchView, basename='search-article')
urlpatterns = [
    path('search/', ArticleSearchView.as_view({'get': 'list'}), name='search-article'),
]