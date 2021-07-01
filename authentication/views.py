from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from .models import User
from .utils import Util
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings
# Create your views here.



class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
   
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relativeLink = reverse(email-verify)
            absurl = 'http://'+current_site+relativeLink+"?token="+token
            email_body = 'Hi '+user.username+' Use link below to verify your email \n'+absurl
            data={'email_body': email_body, 'to_email':user.email ,'email_subject':'Verify your email'}
            Util.send_email(data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
     
class VerifyEmail(GenericAPIView):
    def get(self, request):
        token=request.GEt.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload('user_id'))
            if not user.is_verified:   
                user.is_verified=True
                user.save()
            return Response({'email':'Successfully activated'},status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error':'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error':'Invalid Token Request New One'}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)