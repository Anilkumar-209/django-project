from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# URL patterns for authentication-related endpoints
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # user registration endpoint
    path('login/', TokenObtainPairView.as_view(), name='login'),  # JWT token obtain endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh endpoint
]
