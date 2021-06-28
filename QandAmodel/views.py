from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import AnswerSerializer, QuestionSerializer
from rest_framework import viewsets
from .models import Question, Answer

# Create your views here.

class PostQuestionAPI(LoginRequiredMixin,ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailAPIView(LoginRequiredMixin,RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()    


class AnswerAPI(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
