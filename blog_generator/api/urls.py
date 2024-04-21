from django.urls import path
from . import viewsets

urlpatterns = [
    path("generate/" , viewsets.generate_blog , name="api-request-blog")
]