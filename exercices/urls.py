from django.urls import path, include
from . import views


urlpatterns = [
    # Path to getting the whole list of exercices created 
    path('liste/', views.ExercicesList, name="exercices"),

    # Path to getting the details of one exercice by its ID
    path('details/<str:pk>/', views.ExercicesDetail, name="details"),
    # Path to creating a new exercice
    path('create/', views.ExercicesCreate, name="create"),

    # Path to updating an exercice
    path('update/<str:pk>/', views.ExercicesUpdate, name="update"),

    # Path to deleting an exercice
    path('delete/<str:pk>/', views.ExercicesDelete, name="delete"),
]
