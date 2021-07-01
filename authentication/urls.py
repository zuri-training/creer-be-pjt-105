from authentication import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name="register"),
    path('login/', views.LoginAPIView.as_view(), name="login"),
    path('user/', views.AuthUserAPIView.as_view(), name="user"),
]