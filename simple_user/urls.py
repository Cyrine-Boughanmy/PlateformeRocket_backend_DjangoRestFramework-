from django.urls import path, include
from .views import CreateSimpleUser, SimpleUserCreation
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user/', CreateSimpleUser.as_view()),
    path('register/', SimpleUserCreation.as_view()),

    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    #PATH FOR JWT TOKENS AND URLS
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()), 
]
