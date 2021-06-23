from authentication import views
from django.urls import path, include
from rest_framework import routers
from authentication.views import AnswerAPI, PostQuestionAPI, QuestionDetailAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register("question", PostQuestionAPI)
router.register("answer", AnswerAPI)

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name="register"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('user', views.AuthUserAPIView.as_view(), name="user"),
    path('', include(router.urls)),
    path('posts/<uuid:pk>/', views.QuestionDetailAPIView.as_view(), name='question-detail'),
]