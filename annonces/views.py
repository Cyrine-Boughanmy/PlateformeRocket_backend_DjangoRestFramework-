from rest_framework import generics
from .serializers import AnnonceSerializer
from .models import Annonce

# The ListCreateAPIView gives the ability to get the list of the announcements that are created and to create new ones.
 
# We needed also to override the "perform_create" function to set the owner field to the current user.
class AnnonceList(generics.ListCreateAPIView):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# The RetrieveUpdateDestroyAPIView gives the ability to get by Id, update and delete an announcement within a single entity.
class AnnonceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
