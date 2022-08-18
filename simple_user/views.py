# from lib2to3.pgen2 import token
from rest_framework import generics, permissions
# from django.contrib.auth.models import User
from .models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# from django_filters.rest_framework import DjangoFilterBackend

class SimpleUserList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = UserDetailsSerializer
    queryset = User.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['email',]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer): 
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)

        token['username'] = user.username 
        token['email'] = user.email
        token['first_name'] = user.first_name 
        token['last_name'] = user.last_name 
        token['date_de_naissance'] = user.date_de_naissance 
        token['adresse'] = user.adresse 
        token['code_postal'] = user.code_postal 
        token['ville'] = user.ville 
        token['num_tel'] = user.num_tel 
        # token['profile_image'] = user.profile_image 
        # token['resume'] = user.resume 
        token['presentation'] = user.presentation 
        token['avancement'] = user.avancement 
        return token
class MyTokenObtainPairView(TokenObtainPairView): 
    serializer_class = MyTokenObtainPairSerializer

class SimpleUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

# permission = permissions.AllowAny,
# class CreateSimpleUser(generics.CreateAPIView):
#     permission_classes = (permission)
#     queryset = User.objects.all()
#     serializer_class = RegisterSimpleUserSerializer

# class SimpleUserCreation(generics.CreateAPIView):
#     permission_classes = (permission)
#     queryset = SimpleUser.objects.all()
#     serializer_class = SimpleUserSerializers

# class SimpleUserDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permission)
#     queryset = SimpleUser.objects.all()
#     serializer_class = SimpleUserSerializers

# class SimpleUserList(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = profileSimpleUser
#     queryset = SimpleUser.objects.all()
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['email',]
# class SimpleUserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated,]
#     queryset = SimpleUser.objects.all()
#     serializer_class = profileSimpleUser
