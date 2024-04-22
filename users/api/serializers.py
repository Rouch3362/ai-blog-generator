from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username

        return token
    
class UserToken(TokenObtainPairView):
    serializer_class = TokenSerializer

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username" , "email" , "password")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username" , "email" , "date_joined")