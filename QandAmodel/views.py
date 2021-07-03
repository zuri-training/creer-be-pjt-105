from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import AnswerSerializer, QuestionSerializer
from rest_framework import viewsets, filters
from .models import Question, Answer
from rest_framework import permissions

# Create your views here.

class PostQuestionAPI(LoginRequiredMixin,ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']
    permissions = (permissions.IsAuthenticated, )


class QuestionDetailAPIView(LoginRequiredMixin,RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()   
    permissions = (permissions.IsAuthenticated,)
    lookup_field ="id"

#what is performcreate
class AnswerAPI(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permissions = (permissions.IsAuthenticated,)

