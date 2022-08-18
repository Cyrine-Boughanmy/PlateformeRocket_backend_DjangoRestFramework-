from django.urls import path, include
# from .views import CreateSimpleUser, SimpleUserCreation, SimpleUserDetail, SimpleUserList, SimpleUserDetailView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SimpleUserList, MyTokenObtainPairView, SimpleUserDetailView
urlpatterns = [
    # path('user/', CreateSimpleUser.as_view()),
    # path('register/', SimpleUserCreation.as_view()),
    # path('update_profile/<int:pk>/', SimpleUserDetail.as_view()),
    # path('profile/', SimpleUserList.as_view()), 
    # path('profile/<str:pk>/', SimpleUserDetailView.as_view()), 
    path('users/', SimpleUserList.as_view()),
    path('profile/<str:pk>/', SimpleUserDetailView.as_view()), 


    # path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    #PATH FOR JWT TOKENS AND URLS
    path('token/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()), 
]
