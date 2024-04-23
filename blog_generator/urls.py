from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name="home"),
    path("blogs/" , views.Blogs.as_view() , name="blogs"),
    path("blogs/<int:pk>/" , views.single_blog , name="single-blog")
]