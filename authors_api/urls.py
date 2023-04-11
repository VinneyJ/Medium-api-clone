"""authors_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Authors Medium Clone API",
        default_version = "v1",
        description="API endpoints for the Authors API project",
        contact=openapi.Contact(email="medium.clone@gmail.com"),
        license=openapi.License(name="MIT license")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), 
    name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/articles/", include("core_apps.articles.urls")),
    path("api/v1/ratings/", include("core_apps.ratings.urls")),
    path("api/v1/vote/", include("core_apps.reactions.urls")),
    path("api/v1/favorite/", include("core_apps.favorites.urls")),
    path("api/v1/comments/", include("core_apps.comments.urls")),
    path("api/v1/haystack/", include("core_apps.search.urls")),
]

admin.site.site_header = "Medium Backend API Admin"
admin.site.site_title = "Medium API Admin Portal"
admin.site.index_title = "Welcome to the Medium Backend API clone Portal"