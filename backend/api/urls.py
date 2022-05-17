from django.urls import path 
from . import views 
from blog import views as blogviews



urlpatterns =[
    path('home/', views.api_home),
    path('article/', blogviews.article_init_api),
    path('article/create/', blogviews.create_Article),
]