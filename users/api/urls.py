from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from . import viewsets
from .serializers import UserToken

urlpatterns = [
    path("register/" , viewsets.RegisterUser.as_view()),
    path("users/<str:username>/" , viewsets.single_user , name="api-single-user"),
    # jwt auth routes

    path("login/" , UserToken.as_view() , name="api-login"),
    path("token/refresh/" , TokenRefreshView.as_view() , name="api-token-refresh")
]