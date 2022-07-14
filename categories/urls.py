from django.urls import path, include
from . import views


urlpatterns = [
    # Path to getting the whole list of categories created 
    path('liste/', views.CategorieList, name="categories"),

    # Path to getting the details of one category by its ID
    path('details/<str:pk>/', views.CategorieDetail, name="details"),
    # Path to creating a new category
    path('create/', views.CategorieCreate, name="create"),

    # Path to updating a category
    path('update/<str:pk>/', views.CategorieUpdate, name="update"),

    # Path to deleting a category
    path('delete/<str:pk>/', views.CategorieDelete, name="delete"),
]
