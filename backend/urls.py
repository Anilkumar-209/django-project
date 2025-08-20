"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# home view to redirect root path to /api/docs/
def home(request):
    return redirect('/api/docs/')

urlpatterns = [
    path('', home),  # home view
    path('admin/', admin.site.urls),  # django admin interface
    path('api/users/', include('users.urls')),  # user management routes
    path('api/paragraphs/', include('paragraphs.urls')),  # paragraph features routes
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # openapi schema
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # swagger ui
]
