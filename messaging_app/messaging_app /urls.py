#!/usr/bin/env python3
"""
Main URL configuration for messaging_app project.

Includes:
- Admin site
- API routes from chats app under /api/
- DRF authentication under /api-auth/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),  # ✅ Required: "api/"
    path('api-auth/', include('rest_framework.urls')),  # DRF login view
]



# urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('messaging_app.chats.urls')),  # assuming chats app has its urls
]
