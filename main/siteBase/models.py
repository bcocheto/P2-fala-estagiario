from django.db import models



class Post(models.Model):
    titlePost = models.CharField(max_length=50)
    bodyPost = models.CharField(max_length=200)
    likesPost = models.IntegerField(null=True)
    userName = models.CharField(max_length=64)
