from ..models import Blog
from rest_framework import serializers
from users.api.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):

    owner = UserSerializer()

    class Meta:
        model = Blog
        fields = "__all__"