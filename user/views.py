from django.shortcuts import render,redirect
from datetime import datetime
from .models import User
from .serializers import RegisterSerializer, SigninSerializer
from rest_framework import generics

class UserCreate(generics.CreateAPIView):

    serializer_class = RegisterSerializer

    """ def post(self, request):

        serializer_class = RegisterSerializer
        if serializer_class.is_valid():
            serializer_class.save(user = self.request.user) """

class UserSignin(generics.CreateAPIView):

    
    serializer_class = SigninSerializer
"""     def post(self, request):

        serializer_class = SigninSerializer
        if serializer_class.is_valid():

            user = serializer_class.validated_data
 """

    