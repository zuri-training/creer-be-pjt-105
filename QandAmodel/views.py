from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import AnswerSerializer, QuestionSerializer
from rest_framework import viewsets, filters
from .models import Question, Answer
from rest_framework import permissions

# Create your views here.

class QuestionListAPIView(LoginRequiredMixin,ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serialiizer):
        return serialiizer.save(author=self.request.user)



class QuestionDetailAPIView(LoginRequiredMixin,RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()   
    permission_classes = [permissions.IsAuthenticated]
    lookup_field ="id"
    def perform_create(self, serializer):
        return serialiizer.save(author=self.request.user)


#what is performcreate
class AnswerAPIView(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [permissions.IsAuthenticated]

   