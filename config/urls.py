"""
URL configuration for recordex_be project.
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from config.routers import urlpatterns as api_urlpatterns


token_urlpatterns = [
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]

urlpatterns = [
    path("api/token/", include(token_urlpatterns)),
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
]
