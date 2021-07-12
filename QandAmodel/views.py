from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

# for leke this for only django custom login
# from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import AnswerSerializer, QuestionSerializer
from rest_framework import viewsets, filters
from .models import Question, Answer
from rest_framework import permissions

# Create your views here.


class QuestionListAPIView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']

    def perform_create(self, serialiizer):
        return serialiizer.save(author=self.request.user)


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    lookup_field = "id"

    def perform_create(self, serializer):
        return serialiizer.save(author=self.request.user)


# what is performcreate
class AnswerAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        return serialiizer.save(author=self.request.user)
