from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import SimpleUser
from .serializers import *
from rest_framework.permissions import IsAuthenticated

permission = permissions.AllowAny,
class CreateSimpleUser(generics.CreateAPIView):
    permission_classes = (permission)
    queryset = User.objects.all()
    serializer_class = RegisterSimpleUserSerializer

class SimpleUserCreation(generics.CreateAPIView):
    permission_classes = (permission)
    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializers

class SimpleUserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permission)
    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializers

class SimpleUserList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = profileSimpleUser
    queryset = SimpleUser.objects.all()

class SimpleUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = SimpleUser.objects.all()
    serializer_class = profileSimpleUser
