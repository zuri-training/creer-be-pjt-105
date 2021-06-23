from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from authentication.serializers import AnswerSerializer, RegisterSerializer, LoginSerializer, QuestionSerializer
from rest_framework import response, viewsets
from django.contrib.auth import authenticate
from authentication.models import Question, Answer
# Create your views here.


class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return response.Response({'user':serializer.data})


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
   
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
     
        

class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message':'Invalid Credentials, try again'}, status=status.HTTP_401_UNAUTHORIZED)
        
class PostQuestionAPI(ListCreateAPIView):
    queryset = Question.objects.active()
    serializer_class = QuestionSerializer

class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.active()    


class AnswerAPI(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer    