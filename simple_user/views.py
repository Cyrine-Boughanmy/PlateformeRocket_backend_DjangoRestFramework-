from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import SimpleUser
from .serializers import RegisterSimpleUserSerializer, SimpleUserSerializers

permission = permissions.AllowAny
class CreateSimpleUser(generics.CreateAPIView):
    permission_classes = [permission]
    queryset = User.objects.all()
    serializer_class = RegisterSimpleUserSerializer

class SimpleUserCreation(generics.CreateAPIView):
    permission_classes = [permission]
    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializers