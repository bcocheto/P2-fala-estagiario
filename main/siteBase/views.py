from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import PostForm
from .models import Post


def indexView(request):
    form = PostForm()
    posts = Post.objects.all()
    return render(request, "index.html", {"form": form, "posts": posts})


def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": ""}, status=400)
