from django.urls import path, include
from . import views

urlpatterns = [
    # This url is for listing and creating new comments 
    path('blog/', views.BlogList.as_view()),

    # This url is for listing a comment by its id, update it or delete it. 
    path('blog/<int:pk>/', views.BlogDetail.as_view()),

    # This url is for listing and creating new comments 
    path('commentaire/', views.CommentaireList.as_view()),

    # This url is for listing a comment by its id, update it or delete it. 
    path('commentaire/<int:pk>/', views.CommentaireDetail.as_view()),

    # This url is for testing purposes only 
    path('api-auth/', include('rest_framework.urls')),

]
