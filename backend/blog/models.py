from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Topic(models.Model):
    name= models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = ( ('draft', 'Draft'), ('published', 'Published'))

    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='draft')
    likes = models.IntegerField()
    

    @property
    def author(self):
        return self.owner.username

    @property
    def like(self):
        self.like += 1
        return self.likes

    class Meta:
        ordering = ('-publish',)

    
    def __str__(self):
        return self.title
