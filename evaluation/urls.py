from django.urls import path, include
from . import views


urlpatterns = [
    # Path to getting the whole list of evaluation exercices created 
    path('liste/', views.EvaluationList, name="evalutions"),

    # Path to getting the details of one evaluation exercices by its ID
    path('details/<str:pk>/', views.EvaluationDetail, name="details"),
    # Path to creating a new course
    path('create/', views.EvaluationCreate, name="create"),

    # Path to updating an evaluation exercice 
    path('update/<str:pk>/', views.EvaluationUpdate, name="update"),

    # Path to deleting an evaluation exercice 
    path('delete/<str:pk>/', views.EvaluationDelete, name="delete"),
]
