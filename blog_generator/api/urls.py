from django.urls import path
from . import viewsets

urlpatterns = [
    path("generate/" , viewsets.blog_generator , name="api-request-blog"),
    path("my-blogs/" , viewsets.UserBlog.as_view() , name="api-user-blog"),
    path("blogs/" , viewsets.blogs , name="api-blogs"),
    path("blogs/<int:pk>/" , viewsets.SingleBlog.as_view() , name="api-single-blog")
]