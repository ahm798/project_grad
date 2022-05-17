from django.http import JsonResponse
from .models import Article, Topic
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogSerializer


@api_view(['GET', ])
def article_init_api(request, *args, **kwargs):
    instance = Article.objects.all().order_by('?').first()
    data ={}

    if instance:
        data = BlogSerializer(instance).data
    return Response(data)


@api_view(['POST', ])
def create_Article(request, *args, **kwargs):
    
    data = request.data 
    
    return Response(data)