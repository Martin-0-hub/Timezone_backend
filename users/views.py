from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .Serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .Serializers import EmailTokenObtainPairSerializer

from django.http import HttpResponse   
# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        return Response(UserSerializer(request.user).data)
    
def home(request):
        return HttpResponse("Welcome! The API is running.")

class EmailLoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer



