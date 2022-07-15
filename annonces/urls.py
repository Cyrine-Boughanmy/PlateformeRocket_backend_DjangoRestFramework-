from django.urls import path, include
from . import views

urlpatterns = [
    # This url is for listing and creating new announcements 
    path('annonce/', views.AnnonceList.as_view()),

    # This url is for listing an announcement by its id, update it or delete it. 
    path('annonce/<int:pk>/', views.AnnonceDetail.as_view()),

    # This url is for testing purposes only 
    path('api-auth/', include('rest_framework.urls')),

]
