from rest_framework import serializers
from django.contrib.auth.models import User 


class AccountRegisterationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= User
        fields=['username', 'email', 'password', 'password2']