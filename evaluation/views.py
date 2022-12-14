from .serializers import EvaluationSerializers
from .models import EvaluationClass

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

# Function to obtaining the list of evaluation exercices that were created 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def EvaluationList(request): 
    evaluations = EvaluationClass.objects.all()
    serializer = EvaluationSerializers(evaluations, many = True)
    return Response(serializer.data)

# Function to get an evaluation exercice by its ID 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def EvaluationDetail(request, pk):
    evaluations = EvaluationClass.objects.get(id = pk)
    serializer = EvaluationSerializers(evaluations, many = False)
    return Response(serializer.data)

# Function to Creating a new evaluation exercice 
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def EvaluationCreate(request):
    serializer = EvaluationSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to updating an evaluation exercice 
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def EvaluationUpdate(request, pk):
    evaluations = EvaluationClass.objects.get(id = pk)
    serializer = EvaluationSerializers(instance=evaluations, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to be able to delete an evaluation exercice
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def EvaluationDelete(request, pk):
    evaluations = EvaluationClass.objects.get(id=pk)
    evaluations.delete()

    return Response('Deleted !')