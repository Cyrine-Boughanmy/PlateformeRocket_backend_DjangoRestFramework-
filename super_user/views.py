from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import SuperUser
from .serializers import RegisterSuperUserSerializer, SuperUserSerializers

permission = permissions.AllowAny
class CreateUser(generics.CreateAPIView):
    permission_classes = [permission]
    queryset = User.objects.all()
    serializer_class = RegisterSuperUserSerializer

class SuperUserCreation(generics.CreateAPIView):
    permission_classes = [permission]
    queryset = SuperUser.objects.all()
    serializer_class = SuperUserSerializers