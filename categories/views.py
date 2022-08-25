from .models import Categorie
from .serializers import CategorieSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
# Function to obtaining the list of categories that were created 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CategorieList(request): 
    categories = Categorie.objects.all()
    serializer = CategorieSerializers(categories, many = True)
    return Response(serializer.data)

# Function to get a category by its ID 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CategorieDetail(request, pk):
    categories = Categorie.objects.get(id = pk)
    serializer = CategorieSerializers(categories, many = False)
    return Response(serializer.data)

# Function to Creating a new category 
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CategorieCreate(request):
    serializer = CategorieSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to updating a category 
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CategorieUpdate(request, pk):
    categories = Categorie.objects.get(id = pk)
    serializer = CategorieSerializers(instance=categories, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to be able to delete a category 
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CategorieDelete(request, pk):
    categories = Categorie.objects.get(id=pk)
    categories.delete()

    return Response('Deleted !')