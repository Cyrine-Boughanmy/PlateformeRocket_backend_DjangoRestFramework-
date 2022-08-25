from rest_framework import generics, permissions
# from django.contrib.auth.models import User
from .models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
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
        # token['date_de_naissance'] = user.date_de_naissance 
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, username):
        user = get_object_or_404(User, username=username)
        return user

    def put(self, request):
        
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            user = self.get_object(username)
            new_password = serializer.data['password']
            is_same_as_old = user.check_password(new_password)
            if is_same_as_old:
                """
                old password and new passwords should not be the same
                """
                return Response({"password": ["It should be different from your last password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password)
            user.save()
            return Response({'success':True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # """
    # An endpoint for changing password.
    # """
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # serializer_class = ChangePasswordSerializer
    # model = User

    # def get_object(self, queryset=None):
    #     obj = self.request.user
    #     return obj

    # def update(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     serializer = self.get_serializer(data=request.data)

    #     if serializer.is_valid():
    #         # Check old password
    #         if not self.object.check_password(serializer.data.get("old_password")):
    #             return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
    #         # set_password also hashes the password that the user will get
    #         self.object.set_password(serializer.data.get("new_password"))
    #         self.object.save()
    #         response = {
    #             'status': 'success',
    #             'code': status.HTTP_200_OK,
    #             'message': 'Password updated successfully',
    #             'data': []
    #         }

    #         return Response(response)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class ChangePasswordView(generics.UpdateAPIView):
    
#     # queryset = User.objects.all()
#     # permission_classes = (IsAuthenticated,)
#     serializer_class = ChangePasswordSerializer
#     def update(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
    # def get_object(self, queryset=None):
    #         obj = self.request.user
    #         return obj

    # def update(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     serializer = self.get_serializer(data=request.data)

    #     if serializer.is_valid():
    #         # Check old password
    #         if not self.object.check_password(serializer.data.get("old_password")):
    #             return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
    #         # set_password also hashes the password that the user will get
    #         self.object.set_password(serializer.data.get("new_password"))
    #         self.object.save()
    #         response = {
    #             'status': 'success',
    #             'code': status.HTTP_200_OK,
    #             'message': 'Password updated successfully',
    #             'data': []
    #         }
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
