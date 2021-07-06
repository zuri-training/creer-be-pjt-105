from QandAmodel import views
from django.urls import path, include
# from rest_framework import routers
from .views import QuestionListAPIView, QuestionDetailAPIView, AnswerAPIView




# router = routers.DefaultRouter()
# router.register("answer", AnswerAPI)

urlpatterns = [
    # path('', include(router.urls)),
    path('',QuestionListAPIView.as_view(), name='question-list'),
    path('question/<int:id>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('answer/<int:id>/', AnswerAPIView.as_view, name='answers')
]