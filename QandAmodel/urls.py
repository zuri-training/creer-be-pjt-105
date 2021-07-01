from QandAmodel import views
from django.urls import path, include
from rest_framework import routers
from .views import QuestionDetailAPIView, PostQuestionAPI, AnswerAPI




router = routers.DefaultRouter()
router.register("answer", AnswerAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<uuid:pk>/', views.QuestionDetailAPIView.as_view(), name='question-detail'),
    path('question/<uuid:pk>/', views.PostQuestionAPI.as_view, name='question')
]