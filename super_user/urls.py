from django.urls import path, include
from .views import CreateUser, SuperUserCreation, SuperUserDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user/', CreateUser.as_view()),
    path('register/', SuperUserCreation.as_view()),
    path('update_profile/<int:pk>/', SuperUserDetail.as_view()),


    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    #PATH FOR JWT TOKENS AND URLS
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()), 
]
