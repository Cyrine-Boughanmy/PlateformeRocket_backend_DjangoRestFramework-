from django.shortcuts import render
from .models import Blog, Commentaire
from .serializers import BlogSerializer, CommentaireSerializer
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated

# The ListCreateAPIView gives the ability to get the list of the blogs that are created and to create new ones.
 
# We needed also to override the "perform_create" function to set the owner field to the current user.
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# The RetrieveUpdateDestroyAPIView gives the ability to get by Id, update and delete a blog within a single entity.
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentaireList(generics.ListCreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]