from django.urls import path, include
from . import views


urlpatterns = [
    # Path to getting the whole list of categories created 
    path('liste/', views.CoursList, name="cours"),

    # Path to getting the details of one category by its ID
    path('details/<str:pk>/', views.CoursDetail, name="details"),
    # Path to creating a new category
    path('create/', views.CoursCreate, name="create"),

    # Path to updating a category
    path('update/<str:pk>/', views.CoursUpdate, name="update"),

    # Path to deleting a category
    path('delete/<str:pk>/', views.CoursDelete, name="delete"),
]
