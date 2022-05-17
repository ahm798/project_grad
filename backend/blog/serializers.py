from rest_framework import serializers
from .models import Article, Topic 
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User 
        fields=['id','username']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id','name']



class BlogSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    owner = UserSerializer()
    likes = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Article
        fields = [
            'id',
            'topic',
            'title',
            'owner',
            'slug',
            'publish',
            'created',
            'updated',
            'status',
            'likes',
            'author',
        ]

    def get_likes(self, obj):
        print(obj)
        return obj.likes
    
    def get_author(self, obj):
        return obj.owner.username