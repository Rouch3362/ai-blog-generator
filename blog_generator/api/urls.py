from django.urls import path
from . import viewsets

urlpatterns = [
    path("generate/" , viewsets.blog_generator , name="api-request-blog"),
    path("blogs/" , viewsets.UserBlog.as_view() , name="api-user-blog")
]