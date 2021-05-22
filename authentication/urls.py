from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView,)
from .views import RegisterView, VerifyEmail


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

