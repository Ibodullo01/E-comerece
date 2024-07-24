from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, UpdateAPIView

from .serializers import UserSerializer, UserUpdateSerializer

User = get_user_model()


class SignUp(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
