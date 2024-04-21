from .serializers import CreateUserSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView

class RegisterUser(CreateAPIView):
    serializer_class = CreateUserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()