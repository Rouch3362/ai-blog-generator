from django.urls import path
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path("register/" , views.RegisterUser , name="register"),
    path("login/" , authViews.LoginView.as_view(template_name="login.html") , name="login"),
    path("logout/" , authViews.LogoutView.as_view() , name="logout")
]