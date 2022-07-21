from .serializers import ExerciceSerializers
from .models import Exercices

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Function to obtaining the list of Exercices that were created 
@api_view(['GET'])
def ExercicesList(request): 
    exercices = Exercices.objects.all()
    serializer = ExerciceSerializers(exercices, many = True)
    return Response(serializer.data)

# Function to get an exercice by its ID 
@api_view(['GET'])
def ExercicesDetail(request, pk):
    exercices = Exercices.objects.get(id = pk)
    serializer = ExerciceSerializers(exercices, many = False)
    return Response(serializer.data)

# Function to Creating a new exercice 
@api_view(['POST'])
def ExercicesCreate(request):
    serializer = ExerciceSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to updating an exercice 
@api_view(['PUT'])
def ExercicesUpdate(request, pk):
    exercices = Exercices.objects.get(id = pk)
    serializer = ExerciceSerializers(instance=exercices, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to be able to delete an exercice 
@api_view(['DELETE'])
def ExercicesDelete(request, pk):
    exercices = Exercices.objects.get(id=pk)
    exercices.delete()

    return Response('Deleted !')