from django.contrib import admin
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'author', 'slug', 'article_read_time', 'views']
    list_display_links = ['pkid', 'author']
    # list_filter = ['author', 'created_at', 'updated_at']
    # search_fields = ['title', 'author', 'created_at', 'updated_at']
    # ordering = ['-created_at',]

admin.site.register(models.Article, ArticleAdmin)