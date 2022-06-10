from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('post/ajax/post', views.createPost, name='createPost'),
]
