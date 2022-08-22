from .serializers import CourSerializers, CategorySerializer, ModuleSerializer, SousModuleSerializers
from .models import Cours, Module, SousModule
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


# Function to obtaining the list of courses that were created 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CoursList(request): 
    cours = Cours.objects.all()
    serializer = CourSerializers(cours, many = True)
    return Response(serializer.data)

# Function to get a course by its ID 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CoursDetail(request, pk):
    cours = Cours.objects.get(id = pk)
    serializer = CourSerializers(cours, many = False)
    return Response(serializer.data)

# Function to Creating a new course 
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CoursCreate(request):
    serializer = CourSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to updating a course 
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CoursUpdate(request, pk):
    cours = Cours.objects.get(id = pk)
    serializer = CourSerializers(instance=cours, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Function to be able to delete a course 
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def CoursDelete(request, pk):
    cours = Cours.objects.get(id=pk)
    cours.delete()

    return Response('Deleted !')

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def ModuleList(request): 
    modules = Module.objects.all()
    serializer = ModuleSerializer(modules, many = True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def ModuleDetail(request, pk):
    modules = Module.objects.get(id = pk)
    serializer = ModuleSerializer(modules, many = False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def SousModuleList(request): 
    sousModules = SousModule.objects.all()
    serializer = SousModuleSerializers(sousModules, many = True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def SousModuleDetail(request, pk):
    sousModules = SousModule.objects.get(id = pk)
    serializer = SousModuleSerializers(sousModules, many = False)
    return Response(serializer.data)

# class ListCreateModule(generics.ListCreateAPIView):
#     queryset = Module.objects.all()
#     serializer_class = ModuleSerializer

#     def get_queryset(self):
#         return self.queryset.filter(cours_id = self.kwargs.get('cours_pk'))
    
#     def perform_create(self, serializer):
#         cours = get_object_or_404(Cours, pk = self.kwargs.get('cours_pk'))
#         serializer.save(cours=cours)

# class RetrieveUpdateDestroyModule(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Module.objects.all()
#     serializer_class = ModuleSerializer
    
#     def get_object(self):
#         return get_object_or_404(
#             self.get_queryset(),
#             cours_id=self.kwargs.get('cours_pk'),
#             pk=self.kwargs.get('pk')
#         )
