from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import AccountRegisterationSerializer

class UserRegesterationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountRegisterationSerializer


    def perform_create(self, serializer):
        print(serializer.validated_data)