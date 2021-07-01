from QandAmodel import views
from django.urls import path, include
# from rest_framework import routers
from .views import QuestionDetailAPIView, PostQuestionAPI, AnswerAPI




# router = routers.DefaultRouter()
# router.register("answer", AnswerAPI)

urlpatterns = [
    # path('', include(router.urls)),
    path('',PostQuestionAPI.as_view(), name='question-list'),
    path('question/<uuid:pk>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('answer/<uuid:pk>/', AnswerAPI.as_view, name='question')
]