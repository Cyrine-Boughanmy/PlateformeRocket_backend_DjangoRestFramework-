from .serializers import CourSerializers, CategorySerializer
from .models import Cours

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Function to obtaining the list of courses that were created 
@api_view(['GET'])
def CoursList(request): 
    cours = Cours.objects.all()
    serializer = CourSerializers(cours, many = True)
    return Response(serializer.data)

# Function to get a course by its ID 
@api_view(['GET'])
def CoursDetail(request, pk):
    cours = Cours.objects.get(id = pk)
    serializer = CourSerializers(cours, many = False)
    return Response(serializer.data)

# Function to Creating a new course 
@api_view(['POST'])
def CoursCreate(request):
    serializer = CourSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to updating a course 
@api_view(['PUT'])
def CoursUpdate(request, pk):
    cours = Cours.objects.get(id = pk)
    serializer = CourSerializers(instance=cours, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to be able to delete a course 
@api_view(['DELETE'])
def CoursDelete(request, pk):
    cours = Cours.objects.get(id=pk)
    cours.delete()

    return Response('Deleted !')
