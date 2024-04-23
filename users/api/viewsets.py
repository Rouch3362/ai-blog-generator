from .serializers import CreateUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from blog_generator.api.viewsets import BlogPaginator
from blog_generator.models import Blog
from rest_framework.exceptions import NotFound
from blog_generator.api.serializers import BlogSerializer


class RegisterUser(CreateAPIView):
    serializer_class = CreateUserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

@api_view(["GET"])
def single_user(request , username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise NotFound
    
    blogs = Blog.objects.filter(owner=user)
    paginator = BlogPaginator()
    page = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(page , many=True)

    return paginator.get_paginated_response(serializer.data)
    